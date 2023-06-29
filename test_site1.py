from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# 1. открыть страницу авторизации
# 2. заполнить поле логин
# 3. заполнить поле password
# 4. нажать кнопку Login

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 1
driver.get(URL)

# 2, 3, 4
input_login = driver.find_element(By.ID, "user-name")
input_password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

input_login.send_keys(LOGIN)
input_password.send_keys(PASSWORD)
login_button.click()
pass
