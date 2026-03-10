from pages.login_page import LoginPage


class TestLogin:

    def test_valid_login(self, driver):

        login_page = LoginPage(driver)

        login_page.login("tomsmith", "SuperSecretPassword!")

        message = login_page.get_flash_message()

        assert "You logged into a secure area!" in message


    def test_invalid_username(self, driver):

        login_page = LoginPage(driver)

        login_page.login("invalid_user", "SuperSecretPassword!")

        message = login_page.get_flash_message()

        assert "Your username is invalid!" in message


    def test_invalid_password(self, driver):

        login_page = LoginPage(driver)

        login_page.login("tomsmith", "wrongpassword")

        message = login_page.get_flash_message()

        assert "Your password is invalid!" in message


    def test_empty_credentials(self, driver):

        login_page = LoginPage(driver)

        login_page.login("", "")

        message = login_page.get_flash_message()

        assert "Your username is invalid!" in message