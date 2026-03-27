from sanitize_email_automation import send_keys_to_element, click_element
from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure
import time

class DashboardPage(BasePage):
    Verify_Email="//p[text()='Verify Email']"
    List_validation="//div[text()='List Validation']"
    Add_List="//span[normalize-space()='Add List']"
    Enter_Emails="//textarea[@id='emails']"

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    @allure.step("click on verify email")
    def click_verify_email(self):
        self.click_element(self.Verify_Email)
        print(f"Verify Email is clicked")
        return True

    @allure.step("Click on List Validation")
    def click_file_validation(self):
        self.click_element(self.List_validation)
        print(f"List validation Clicked")

    @allure.step("click on add list")
    def click_add_list(self):
        self.click_element(self.Add_List)
        print(f"add list clicked")

    @allure.step("send emails on enter emails")
    def enter_emails(self, emails):
        self.click_element(self.Enter_Emails)
        send_keys_to_element(self.Enter_Emails, emails)
        print(f"Emails entered: {emails}")