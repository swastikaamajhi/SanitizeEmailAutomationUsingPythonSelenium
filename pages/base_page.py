from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import allure
import time

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)

    @allure.step("click on element with xpath:{xpath}")
    def click_element(self, xpath):
        element=self.wait.until(EC.element_to_be_clickable((By.XPATH,xpath)))
        assert element.is_displayed(), f"Element with xpath {xpath} is not visible"
        element.click()
        print(f"Successfully clicked on element: {xpath}")

    @allure.step("send keys '{keys}' to element with xpath: {xpath}")
    def send_keys_to_element(self, xpath, keys):
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.send_keys(keys)

    @allure.step("Assert element exists with xpath {xpath}")
    def assert_element_exist(self, xpath, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            assert element.is_displayed(), f"Element with xpath {xpath} is not visible"
            print(f"Assertion passed: Element {xpath} exists and is visible")
            return True
        except:
            print(f"Assertion failed: Element {xpath} does not exist or is not visible")
            return False

    @allure.step("Wait for element to be visible: {xpath}")
    def wait_for_element(self, xpath,timeout):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    @allure.step("Get element text: {xpath}")
    def get_element_text(self, xpath):
        element=self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        return element.text