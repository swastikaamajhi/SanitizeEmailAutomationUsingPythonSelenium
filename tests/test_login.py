from pages .home_page import HomePage
from pages .login_page import LoginPage

def test_login(driver):
    driver.get("https://sanitizeemail.com/")

    home=HomePage(driver)

    login=LoginPage(driver)

    home.click_login_link()

    login.enter_login_credentials("majhiswastika715@gmail.com","Swastika@123")

    login.click_on_checkbox()

    login.click_login()
