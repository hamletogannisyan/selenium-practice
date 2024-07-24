from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL="https://lks.bmstu.ru/"

def test_auth_with_correct_data():
    driver=webdriver.Chrome()
    driver.get("https://lks.bmstu.ru/")
    button_auth1=driver.find_element(By.CSS_SELECTOR, ".p3h_login-trigger")
    button_auth1.click()
    input_login=driver.find_element(By.ID, "username")
    input_password = driver.find_element(By.ID, "password")
    input_login.send_keys("ogv21r141")
    input_password.send_keys("pyezyvdv")
    button_auth2=driver.find_element(By.NAME, "submit")
    button_auth2.click()
    current_url=driver.current_url
    assert current_url=="https://lks.bmstu.ru/profile"

# def test_auth_with_incorrect_password():
#     pass
#
# def test_auth_with_incorrect_password():
#     pass
