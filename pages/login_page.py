from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from support.assertions import Assertions
from config import Secrets, URL


class LoginPage(BaseObject):
    USER_NAME_FIELD = (By.CSS_SELECTOR, '#user_login')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#user_pass')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#wp-submit')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '#error_message')

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions

    def enter_user_name(self, user_name=Secrets.USER_NAME_CLIENT):
        self.send_keys(self.USER_NAME_FIELD, user_name)

    def enter_password(self, password=Secrets.PASSWORD_CLIENT):
        self.send_keys(self.PASSWORD_FIELD, password)

    def click_button(self):
        self.click(self.LOGIN_BUTTON)

    def is_url_valid(self):
        self.assertion.assert_equal(
            expected=URL.PROFILE_PAGE,
            actual=self.get_current_url()
        )

    def is_error_message_correct(self, message):
        self.assertion.assert_equal(
            expected=message,
            actual=self.get_text(self.ERROR_MESSAGE),
            error_type='url'
        )
