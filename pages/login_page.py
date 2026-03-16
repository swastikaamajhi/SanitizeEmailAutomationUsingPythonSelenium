from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure
import time

class LoginPage(BasePage):
    Email_Input="//input[@type='text']"
    Password_Input="//input[@type='password']"
    Checkbox="//button[@role='checkbox']"
    Login_Button="//button[@type='submit']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    @allure.step("Enter login credentials")
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

    @allure.step("Click Login button")
    def click_login(self):
        self.click_element(self.Login_Button)
        print(f"Click on login button")
        return True