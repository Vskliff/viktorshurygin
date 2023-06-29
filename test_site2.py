from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://www.saucedemo.com/'
login = 'standard_user'
password = 'secret_sauce'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(url)

try:
    input_login = driver.find_element(By.ID, "user-name")
    input_password = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    input_login.send_keys(login)
    input_password.send_keys(password)
    login_button.click()
except NoSuchElementException as e:
    print("Element not found:", e)
