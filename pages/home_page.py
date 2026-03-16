from .base_page import BasePage
from selenium.webdriver.common.by import By
import allure

class HomePage(BasePage):
    signup_link="//button[normalize-space()='Sign Up']"
    Login_Link="//button[normalize-space()='Log In']"
    def __init__(self,driver):
        super().__init__(driver)

    @allure.step("Navigate to home page")
    def navigate_to_home(self):
        self.driver.get("https://sanitizeemail.com/")

    @allure.step("click on signup link")
    def click_signup_link(self):
        self.click_element(self.signup_link)

    @allure.step("click on login button")
    def click_login_link(self):
        self.click_element(self.Login_Link)