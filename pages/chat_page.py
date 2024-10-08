from selenium.webdriver.common.by import By
from support.assertions import Assertions
from pages.login_page import LoginPage


class ChatPage(LoginPage):
    CHAT_INPUT = (By.CSS_SELECTOR, '#chat-text')
    SEND_BUTTON = (By.CSS_SELECTOR, '.chat-send-button')
    URGENT_FLAG = (By.CSS_SELECTOR, '#urgent_flag')
    UPLOAD_BUTTON = (By.ID, "file-upload")
    SUBMIT_BUTTON = (By.ID, "file-submit")
    UPLOADED_FILES = (By.ID, "uploaded-files")
    CHAT = (By.CSS_SELECTOR, '.sent:last-child .content_text span')

    def __init__(self, driver):
        super().__init__(driver)
        self.assertion = Assertions

    def enter_message(self, text):
        self.send_keys(self.CHAT_INPUT, text)

    def set_urgent_flag(self):
        self.click(self.URGENT_FLAG)

    def send_message(self):
        self.click(self.SEND_BUTTON)

    def send_text_and_image(self, image):
        self.send_keys(self.CHAT_INPUT, image)

    def log_in(self):
        self.enter_user_name()
        self.enter_password()
        self.click_button()

    def is_message_sent(self, message):
        self.assertion.assert_equal(
            expected=message,
            actual=self.get_text(self.CHAT),
            error_type='message'
        )