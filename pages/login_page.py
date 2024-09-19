from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, '#user_login')
    PASSWORD = (By.CSS_SELECTOR, '#user_pass')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#wp-submit')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '#error_message')

    def login(self, username, password):
        self.find_element(self.USERNAME).send_keys(username)
        self.find_element(self.PASSWORD).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
