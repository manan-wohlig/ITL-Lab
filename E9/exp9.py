from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com/")
search_bar = driver.find_element('name','q')
search_bar.clear()
search_bar.send_keys("news")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)

time.sleep(2)

driver.execute_script("window.open('about:blank', 'secondtab');")
driver.switch_to.window("secondtab")
driver.get('https://www.wikipedia.org/')
print(driver.current_url)
search_bar = driver.find_element('name','search')
search_bar.clear()
search_bar.send_keys("covid")
val = search_bar.get_attribute("value")
print(len(val))
time.sleep(5)
search_bar.send_keys(Keys.RETURN)

content = driver.find_elements(By.TAG_NAME,'p')
for data in content:
    print(data.text)

time.sleep(2)

driver.execute_script("window.open('about:blank', 'thirdtab');")
driver.switch_to.window("thirdtab")
driver.get('https://www.wikipedia.org/')
try:
    driver.find_element('name','searchbox')
except NoSuchElementException:
    print("\n\nElement not found")

time.sleep(10)
driver.quit()


