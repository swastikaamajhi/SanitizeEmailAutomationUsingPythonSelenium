from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import time

class LoginPage(BasePage):
    URL="https://app.sanitizeemail.com/login"
    Email_Input="//input[@name='email']"
    Password_Input="//input[@name='password']"
    Checkbox="//button[@role='checkbox']"
    Login_Button="//button[text()='Log In']"


    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    @allure.step("click on Login credential")
    def enter_login_credentials(self,email,password):
        self.send_keys_to_element(self.Email_Input, email)
        print(f"Email entered: {email}")

        self.send_keys_to_element(self.Password_Input, password)
        print(f"Password entered: {password}")

    @allure.step("Click on checkbox")
    def click_on_checkbox(self):
        self.click_element(self.Checkbox)
        print(f"checkbox is clicked")
        return True

    @allure.step("Click on LOgin")
    def click_login(self):
        self.click_element(self.Login_Button)
        print("Clicked on login button")
        return True

