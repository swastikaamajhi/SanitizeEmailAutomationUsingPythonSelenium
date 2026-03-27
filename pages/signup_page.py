from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import time

class SignupPage(BasePage):
    URL="https://app.sanitizeemail.com/login"
    Signup_Link="//a[text()='Sign Up']"
    Name_Input="//input[@name='username']"
    Email_Input="//input[@name='email']"
    Password_Input="//input[@name='password']"
    Checkbox="//button[@role='checkbox']"
    Signup_button="//button[normalize-space(text())='Sign Up']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    @allure.step("Click on Signup link")
    def click_signup_link(self):
        self.click_element(self.Signup_Link)
        print(f"Signup link clicked")

    @allure.step("click on signup credential")
    def enter_signup_credentials(self,name,email,password):
        self.send_keys_to_element(self.Name_Input, name)
        print(f"Name entered: {name}")

        self.send_keys_to_element(self.Email_Input, email)
        print(f"Email entered: {email}")

        self.send_keys_to_element(self.Password_Input, password)
        print(f"Password entered: {password}")

    @allure.step("Click on checkbox")
    def click_on_checkbox(self):
        self.click_element(self.Checkbox)
        print(f"checkbox is clicked")
        return True

    @allure.step("Click on Signup Button")
    def click_signup_button(self):
        self.click_element(self.Signup_button)
        print("Clicked on Signup button")
        return True

