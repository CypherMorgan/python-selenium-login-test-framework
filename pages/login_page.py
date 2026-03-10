from selenium.webdriver.common.by import By
from utils.wait_utils import WaitUtils
from utils.logger import get_logger


class LoginPage:

    def __init__(self, driver):

        self.driver = driver
        self.wait = WaitUtils(driver)

        self.logger = get_logger(__name__)

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.radius")
    FLASH_MESSAGE = (By.ID, "flash")

    def enter_username(self, username):

        self.logger.info("Entering username")

        username_field = self.wait.wait_for_element_visible(self.USERNAME_INPUT)

        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):

        self.logger.info("Entering password")

        password_field = self.wait.wait_for_element_visible(self.PASSWORD_INPUT)

        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):

        self.logger.info("Clicking login button")

        login_btn = self.wait.wait_for_clickable(self.LOGIN_BUTTON)

        login_btn.click()

    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_flash_message(self):

        self.logger.info("Fetching flash message")

        message = self.wait.wait_for_element_visible(self.FLASH_MESSAGE)

        return message.text