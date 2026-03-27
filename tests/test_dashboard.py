from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_dashboard(driver):

    # Login
    login_page = LoginPage(driver)
    driver.get("https://app.sanitizeemail.com/login")
    login_page.enter_login_credentials("majhiswastika715@gmail.com", "Swastika@123")
    login_page.click_on_checkbox()
    login_page.click_login()

    # Dashboard
    dashboard_page = DashboardPage(driver)
    dashboard_page.click_verify_email()
    dashboard_page.click_file_validation()
    dashboard_page.click_add_list()
    dashboard_page.enter_emails( "test1@gmail.com\ninvalid-email\nabc@domain\ntest_123@outlook.com")