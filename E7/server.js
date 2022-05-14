if (process.env.NODE_ENV !== 'production') {
    require('dotenv').config()
}

const express = require('express')
const app = express()
const bcrypt = require('bcrypt')
const passport = require('passport')
const flash = require('express-flash')
const session = require('express-session')
const cookieSession = require('cookie-session')
require('./oauth')
require('./facebook')
require('./twitter')

const initializePassport = require('./passport-config')
initializePassport(
    passport, 
    email => users.find(user => user.email === email),
    id => users.find(user => user.id === id)
)

const users = []

app.set('view-engine', 'ejs')
app.use(express.urlencoded({ extended: false }))
app.use(flash())
app.use(session({
    secret: process.env.SESSION_SECRET,
    resave: false,
    saveUninitialized: false
}))
app.use(passport.initialize())
app.use(passport.session())
app.use(express.static(__dirname + '/public'))

app.get('/', (req,res) => {
    res.render('index.ejs')
})

app.get('/auth/google',
  passport.authenticate('google', { scope: [ 'email', 'profile' ] }
));

app.get( '/auth/google/movie',
  passport.authenticate( 'google', {
    successRedirect: '/movie',
    failureRedirect: '/'
  })
);

app.get('/auth/facebook', passport.authenticate('facebook'));

app.get('/auth/facebook/movie',
  passport.authenticate('facebook', { failureRedirect: '/login' }),
  function(req, res) {
    // Successful authentication, redirect home.
    res.redirect('/movie');
  });

app.get('/auth/twitter',passport.authenticate('twitter'));

app.get('/auth/twitter/movie', 
  passport.authenticate('twitter', { 
      successRedirect: '/movie',
      failureRedirect: '/' 
    })
  );

app.get('/login', checknotAuthenticated, (req,res) => {
    res.render('login.ejs')
})

app.post('/login', checknotAuthenticated, passport.authenticate('local', {
    successRedirect: '/movie',
    failureRedirect: '/login',
    failureFlash: true
}))

app.get('/register', checknotAuthenticated, (req,res) => {
    res.render('register.ejs')
})

app.post('/register', checknotAuthenticated, async (req,res) => {
    try{
        const hashedPassword = await bcrypt.hash(req.body.password, 10)
        users.push({
            id: Date.now().toString(),
            name: req.body.name,
            email: req.body.email,
            password: hashedPassword
        })
        res.redirect('/login')
    } catch {
        res.redirect('/register')
    }
    console.log(users)
})

app.get('/movie', checkAuthenticated, (req, res) => {
    res.sendFile(__dirname + '/public/home.html')
})

function checkAuthenticated(req, res, next) {
    if (req.isAuthenticated()){
        return next()
    }

    res.redirect('/login')
}

function checknotAuthenticated(req, res, next) {
    if (req.isAuthenticated()){
        return res.redirect('/movie')
    }

    next()
}

app.get('/logout', (req, res) => {
    req.logout();
    req.session.destroy();
    res.redirect("/");
  });  

app.listen(3000)