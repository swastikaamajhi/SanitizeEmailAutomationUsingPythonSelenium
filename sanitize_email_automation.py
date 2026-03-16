# import time
# import allure
# import pytest
#
# from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
#
# driver = webdriver.Chrome(options=chrome_options)
#
# driver.get("https://sanitizeemail.com/")
# @allure.step("click on element with xpath: {xpath}")
# def click_element(driver, xpath):
#     element=driver.find_element(By.XPATH, xpath)
#     assert element.is_displayed(), f"Element with xpath {xpath} is not visible"
#     element.click()
#     print(f"Successfully clicked on element: {xpath}")
# @allure.step("send key '{keys}' to element with xpath: {xpath}")
# def send_keys_to_element(driver, xpath, keys):
#     element=driver.find_element(By.XPATH, xpath)
#     assert element.is_displayed(), f"Element with xpath {xpath}"
#     element.clear()
#     element.send_keys(keys)
#     print(f"successfully sent keys '{keys}' to element :{xpath}")
#
# @allure.step("Assert element exist with xpath:{xpath}")
# def assert_element_exists(driver, xpath, timeout=10):
#     try:
#         WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
#         element=driver.find_element(By.XPATH, xpath)
#         assert element.is_displayed(), f"Element with xpath :{xpath} is not visible"
#         print(f"Assertion passed: Element {xpath} exists and is visible")
#         return  True
#     except:
#         print(f"Assertion failed: Element {xpath} does not exist or is visible")
#         return False
#
# sign_up_data=[
#     {
#         "name": "Swastika Majhi",
#         "email": "majhiswastika715@gmail.com",
#         "password": "Swastika@123"
#     }
# ]
#
# @allure.feature('sanitize email automation')
# @allure.story("User Registration")
# def perform_registration():
#     with allure.step("Running registration test with unique email"):
#         print("Running registration test with unique email")
#
#         driver.get("https://sanitizeemail.com/")
#         time.sleep(5)
#
#         signup="//button[normalize-space()='Sign Up']"
#         assert_element_exists(driver, signup)
#         click_element(driver, signup)
#         print(f"Clicked on signup link")
#         time.sleep(2)
#
#         if "register" in driver.current_url:
#             with allure.step("Registration form loaded successfully"):
#                 print("Registration form loaded successfully")
#         else:
#             with allure.step("warning: Registration form may not have loaded properly"):
#                 print("Warning: registration form may not have loaded properly _ current URL:", driver.current_url)
#
#         name="//input[@type='text']"
#         assert_element_exists(driver,name)
#         send_keys_to_element(driver,name, "swastika majhi")
#
#         email="//input[@id='«r7»-form-item']"
#         assert_element_exists(driver, email)
#         unique_email=f"testuser_{int(time.time())}@gmail.com"
#         send_keys_to_element(driver, email,"majhiswastika715@gmail.com")
#         time.sleep(2)
#
#         password="//input[@id='«r8»-form-item']"
#         assert_element_exists(driver, password)
#         send_keys_to_element(driver, password, "Swastika@123")
#         time.sleep(2)
#
#         checkbox="//button[@id='«r9»-form-item']"
#         assert checkbox.is_selected(), "checkbox is not selected"
#         click_element(driver,checkbox)
#         time.sleep(2)
#
#         signup_button="//button[normalize-space()='Sign Up']"
#         if assert_element_exists(driver, signup_button):
#             click_element(driver,signup_button)
#         else:
#             print("signup button not found")
#         time.sleep(2)
#
# # def click_element(driver, xpath):
# #     element = driver.find_element(By.XPATH, xpath)
# #     element.click()
# #
# # def send_keys_to_element(driver, xpath, keys):
# #     element = driver.find_element(By.XPATH, xpath)
# #     element.send_keys(keys)
# #
# # # SignUp Page
# # time.sleep(10)
# # signup="//button[normalize-space()='Sign Up']"
# # click_element(driver, signup)
# # time.sleep(5)
# #
# # name = "//input[@type='text']"
# # click_element(driver, name)
# # send_keys_to_element(driver, name, "swastika")
# # time.sleep(2)
# #
# # email="//input[@id='«r7»-form-item']"
# # click_element(driver, email)
# # send_keys_to_element(driver, email,"majhiswastika715@gmail.com")
# # time.sleep(2)
# #
# # password="//input[@id='«r8»-form-item']"
# # click_element(driver,password)
# # send_keys_to_element(driver, password, "Swastika@123")
# # time.sleep(2)
# #
# # checkbox="//button[@id='«r9»-form-item']"
# # click_element(driver,checkbox)
# # time.sleep(2)
# #
# # signup_button="//button[normalize-space()='Sign Up']"
# # click_element(driver,signup_button)
# # time.sleep(2)
#
# time.sleep(5)
# driver.quit()

import time
import allure

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)


@allure.step("Click element with xpath: {xpath}")
def click_element(xpath):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    assert element.is_displayed(), f"Element {xpath} is not visible"
    element.click()
    print(f"Clicked element: {xpath}")


@allure.step("Send keys '{keys}' to element: {xpath}")
def send_keys_to_element(xpath, keys):
    element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element.clear()
    element.send_keys(keys)
    print(f"Sent keys '{keys}' to element: {xpath}")


@allure.step("Assert element exists: {xpath}")
def assert_element_exists(xpath):
    element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    assert element.is_displayed(), f"Element {xpath} not visible"
    print(f"Assertion passed: {xpath} exists")
    return element


@allure.feature("Sanitize Email Automation")
@allure.story("User Registration")
def perform_registration():

    with allure.step("Open website"):
        driver.get("https://sanitizeemail.com/")
        print("Website opened")

    with allure.step("Click signup button"):
        signup = "//button[normalize-space()='Sign Up']"
        click_element(signup)

    with allure.step("Fill registration form"):

        name = "//input[@type='text']"
        send_keys_to_element(name, "Swastika Majhi")

        email = "//input[@id='«r7»-form-item']"
        send_keys_to_element(email, "majhiswastika715@gmail.com")

        password = "//input[@type='password']"
        send_keys_to_element(password, "Swastika@123")

    with allure.step("Click terms checkbox"):
        checkbox = "//button[@id='«r9»-form-item']"
        click_element(checkbox)

    with allure.step("Submit registration"):
        signup_button = "//button[normalize-space()='Sign Up']"
        click_element(signup_button)

    time.sleep(3)
    print("Registration test completed")


perform_registration()
driver.quit()
