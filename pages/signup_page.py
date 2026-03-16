from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class SignupPage(BasePage):
    Name_Input="//input[@type='text']"
    Email_Input="//input[@id='«r7»-form-item']"
    Password_Input= "//input[@type='password']"
    Checkbox_Input="//button[@id='«r9»-form-item']"
    Signup_button="//button[normalize-space()='Sign Up']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    @allure.step("click on signup link for registration")
    def fill_registration_form(self,name,email,password):
        self.send_keys_to_element(self.Name_Input, name)
        print(f"Name entered: {name}")

        self.send_keys_to_element(self.Email_Input, email)
        print(f"email entered: {email}")

        self.send_keys_to_element(self.Password_Input, password)
        print(f"password entered: {password}")

    @allure.step("Click on checkbox")
    def click_checkbox(self,):
        self.click_element(self.Checkbox_Input)
        print(f"checkbox clicked")

    @allure.step("click on signup button")
    def click_signup(self, signup):
        self.click_element(self.Signup_button)
        print(f"Signup button clicked")


