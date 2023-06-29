from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# 1. Зайти на главню страницу
# 2. Заполнить поле username
# 3. Заполнить поле password
# 4. Нажать кнопку login

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver
def open_page(driver, URL):
    driver.get(URL)

def get_element_by_id(driver, locator):
    return driver.find_element(By.ID, locator)
def element_click(driver, locator):
    element = get_element_by_id(driver, locator)
    element.click()
def element_send_keys(driver, locator, text):
    element = get_element_by_id(driver, locator)
    element.send_keys(text)
#1
driver = get_driver()
open_page(driver,URL)

#2-3
element_send_keys(driver,'user-name', LOGIN)
element_send_keys(driver,'password', PASSWORD)

#4
element_click(driver, 'login-button')
