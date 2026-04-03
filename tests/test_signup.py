from pages.signup_page import SignupPage

def test_signup(driver):
    signup_page=SignupPage(driver)
    driver.get("https://app.sanitizeemail.com/login")
    signup_page.click_signup_link()
    signup_page.enter_signup_credentials("swastika Majhi", "majhiswastika715@gmail.com", "Swastika@123")
    signup_page.click_on_checkbox()
    signup_page.click_signup_button()