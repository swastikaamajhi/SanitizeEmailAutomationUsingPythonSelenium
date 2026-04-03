from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    driver.get("https://app.sanitizeemail.com/login")
    login_page.enter_login_credentials("majhiswastika715@gmail.com", "Swastika@123")
    login_page.click_on_checkbox()
    login_page.click_login()