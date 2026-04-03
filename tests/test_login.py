import allure

from pages.login_page import LoginPage


class TestLoginPage:
    @allure.title("Login with valid credentials")
    def test_login(self, page):
        login_page = LoginPage(page)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in page.url

    @allure.title("Login with invalid credentials")
    def test_login_invalid(self, page):
        login_page = LoginPage(page)

        login_page.open()
        login_page.login("wrong_user", "wrong_password")

        assert "Username and password" in login_page.get_error_message()
