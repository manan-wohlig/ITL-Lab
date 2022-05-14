from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time

def Test1():
    # Successful test case
    PATH = "D:\Chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("http://localhost/HotelMS-PHP/")

    email_bar = driver.find_element('name', 'email')
    email_bar.clear()
    email_bar.send_keys("aamey")

    password_bar = driver.find_element('name', 'password')
    password_bar.clear()
    password_bar.send_keys("aamey")

    login_button = driver.find_element('name', 'login')
    login_button.click()
    time.sleep(2)

    reservation = driver.find_element(By.LINK_TEXT, 'Reservation')
    reservation.click()
    select = Select(driver.find_element('id', 'room_type'))
    select.select_by_visible_text('Single')

    room_no = Select(driver.find_element('id', 'room_no'))
    room_no.select_by_visible_text('A-719')

    check_in = driver.find_element('id', 'check_in_date')
    check_in.click()
    day = driver.find_elements(By.TAG_NAME, 'tr')
    for date in day:
        if date.text == 10:
            date.click()

    check_out = driver.find_element('id', 'check_out_date')
    check_out.click()
    day = driver.find_elements(By.TAG_NAME, 'tr')
    for date in day:
        if date.text == 15:
            date.click()


    f_name = driver.find_element('id', 'first_name')
    f_name.clear()
    f_name.send_keys("Raj")

    l_name = driver.find_element('id', 'last_name')
    l_name.clear()
    l_name.send_keys("Sharma")

    email = driver.find_element('id', 'email')
    email.clear()
    email.send_keys("raj@gmail.com")

    contact = driver.find_element('id', 'contact_no')
    contact.clear()
    contact.send_keys("9787213746")

    id_type = Select(driver.find_element('id', 'id_card_id'))
    id_type.select_by_visible_text('Pan Card')

    id_no = driver.find_element('id', 'id_card_no')
    id_no.clear()
    id_no.send_keys("1234567890")

    address = driver.find_element('id', 'address')
    address.clear()
    address.send_keys("Mumbai")

    button = driver.find_element('name', 'login')
    button.click()
    time.sleep(3)

    driver.execute_script("window.open('about:blank', 'secondtab');")
    driver.switch_to.window("secondtab")
    driver.get('http://localhost/phpmyadmin/index.php?route=/sql&server=1&db=hotelms&table=customer&pos=0')

    time.sleep(10)
    driver.quit()


def Test2():
    # Failed test case due to incorrect login page element
    PATH = "D:\Chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("http://localhost/HotelMS-PHP/")

    try:
        email_bar = driver.find_element('name', 'emailid')
        email_bar.clear()
        email_bar.send_keys("aamey")

        password_bar = driver.find_element('name', 'password')
        password_bar.clear()
        password_bar.send_keys("aamey")

        login_button = driver.find_element('name', 'login')
        login_button.click()
    except NoSuchElementException:
        print("\n\nLogin error")
        driver.get("http://localhost/HotelMS-PHP/")

    time.sleep(10)
    driver.quit()


def Test3():
    # Failed test case due to element not found
    PATH = "D:\Chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("http://localhost/HotelMS-PHP/")

    try:
        email_bar = driver.find_element('name', 'email')
        email_bar.clear()
        email_bar.send_keys("aamey")

        password_bar = driver.find_element('name', 'password')
        password_bar.clear()
        password_bar.send_keys("aamey")

        login_button = driver.find_element('name', 'login')
        login_button.click()
        time.sleep(2)

        reservation = driver.find_element(By.LINK_TEXT, 'Book Room')
        reservation.click()

    except NoSuchElementException:
        print("\n\n Element not found")

    time.sleep(10)
    driver.quit()


def Test4():
    # Insufficient Length
    PATH = "D:\Chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("http://localhost/HotelMS-PHP/")

    email_bar = driver.find_element('name', 'email')
    email_bar.clear()
    email_bar.send_keys("aamey")

    password_bar = driver.find_element('name', 'password')
    password_bar.clear()
    password_bar.send_keys("aamey")

    login_button = driver.find_element('name', 'login')
    login_button.click()
    time.sleep(2)

    reservation = driver.find_element(By.LINK_TEXT, 'Reservation')
    reservation.click()

    select = Select(driver.find_element('id', 'room_type'))
    select.select_by_visible_text('Double')

    room_no = Select(driver.find_element('id', 'room_no'))
    room_no.select_by_visible_text('D-719')

    check_in = driver.find_element('id', 'check_in_date')
    check_in.click()
    day = driver.find_elements(By.TAG_NAME, 'tr')
    for date in day:
        if date.text == 10:
            date.click()

    check_out = driver.find_element('id', 'check_out_date')
    check_out.click()
    day = driver.find_elements(By.TAG_NAME, 'tr')
    for date in day:
        if date.text == 15:
            date.click()

    f_name = driver.find_element('id', 'first_name')
    f_name.clear()
    f_name.send_keys("Raj")

    l_name = driver.find_element('id', 'last_name')
    l_name.clear()
    l_name.send_keys("Sharma")

    email = driver.find_element('id', 'email')
    email.clear()
    email.send_keys("raj@gmail.com")

    contact = driver.find_element('id', 'contact_no')
    contact.clear()
    contact.send_keys("97813746")
    val = contact.get_attribute("value")
    if len(val) < 10:
        print("Length of phone number is insufficient")

    id_type = Select(driver.find_element('id', 'id_card_id'))
    id_type.select_by_visible_text('Pan Card')

    id_no = driver.find_element('id', 'id_card_no')
    id_no.clear()
    id_no.send_keys("1234567890")

    address = driver.find_element('id', 'address')
    address.clear()
    address.send_keys("Mumbai")

    button = driver.find_element('name', 'login')
    button.click()

    time.sleep(10)
    driver.quit()


def Test5():
    PATH = "D:\Chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("http://localhost/HotelMS-PHP/")

    email_bar = driver.find_element('name', 'email')
    email_bar.clear()
    email_bar.send_keys("aamey")

    password_bar = driver.find_element('name', 'password')
    password_bar.clear()
    password_bar.send_keys("aamey")

    login_button = driver.find_element('name', 'login')
    login_button.click()
    time.sleep(2)

    reservation = driver.find_element(By.LINK_TEXT, 'Reservation')
    reservation.click()
    select = Select(driver.find_element('id', 'room_type'))
    select.select_by_visible_text('Family')

    room_no = Select(driver.find_element('id', 'room_no'))
    room_no.select_by_visible_text('A-104')

    check_in = driver.find_element('id', 'check_in_date')
    check_in.click()
    day = driver.find_elements(By.TAG_NAME, 'tr')
    for date in day:
        if date.text == 10:
            date.click()

    check_out = driver.find_element('id', 'check_out_date')
    check_out.click()
    day = driver.find_elements(By.TAG_NAME, 'tr')
    for date in day:
        if date.text == 15:
            date.click()

    f_name = driver.find_element('id', 'first_name')
    val = f_name.get_attribute("value")
    if len(val) == 0:
        print("\n\nDo not keep the name field empty\nPlease enter a name")

    l_name = driver.find_element('id', 'last_name')
    l_name.clear()
    l_name.send_keys("Sharma")

    email = driver.find_element('id', 'email')
    email.clear()
    email.send_keys("raj@gmail.com")

    contact = driver.find_element('id', 'contact_no')
    contact.clear()
    contact.send_keys("9787213746")

    id_type = Select(driver.find_element('id', 'id_card_id'))
    id_type.select_by_visible_text('Pan Card')

    id_no = driver.find_element('id', 'id_card_no')
    id_no.clear()
    id_no.send_keys("1234567890")

    address = driver.find_element('id', 'address')
    address.clear()
    address.send_keys("Mumbai")

    button = driver.find_element('name', 'login')
    button.click()

    time.sleep(10)
    driver.quit()


def Test6():
    PATH = "D:\Chromedriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("http://localhost/HotelMS-PHP/")

    element = driver.find_element(By.TAG_NAME,'label')
    assert element.text == 'Username or email'

    email_bar = driver.find_element('name', 'email')
    email_bar.clear()
    email_bar.send_keys("aamey")

    password_bar = driver.find_element('name', 'password')
    password_bar.clear()
    password_bar.send_keys("aamey")

    login_button = driver.find_element('name', 'login')
    login_button.click()
    time.sleep(2)

    element = driver.find_element(By.TAG_NAME, 'a')
    assert element.text == 'Replan Booking'

    time.sleep(5)
    driver.quit()


Test6()
Test1()
Test2()
Test3()
Test4()
Test5()