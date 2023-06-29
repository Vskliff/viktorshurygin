from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 1. Зайти на главню страницу
# 2. Заполнить поле username
# 3. Заполнить поле password
# 4. Нажать кнопку login

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

#1
driver.get(URL)

#2
input_login = driver.find_element(By.ID, 'user-name')
input_login.send_keys(LOGIN)
#3
input_password = driver.find_element(By.ID, 'password')
input_password.send_keys(PASSWORD)

#4
login_button = driver.find_element(By.ID, 'login-button')
login_button.click()
