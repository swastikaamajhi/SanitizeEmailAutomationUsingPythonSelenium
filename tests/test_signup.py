from pages.home_page import HomePage
from pages.signup_page import SignupPage

def test_signup(driver):

    driver.get("https://sanitizeemail.com/")

    home = HomePage(driver)
    signup = SignupPage(driver)

    home.click_signup_link()

    signup.fill_registration_form("Swastika","majhiswastika715@gmail.com","Swastika@123")

    signup.click_checkbox()

    signup.click_signup('')