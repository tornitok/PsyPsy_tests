from selenium.webdriver.common.by import By


class LoginPage:
    USERNAME = (By.CSS_SELECTOR, '#user_login')
    PASSWORD = (By.CSS_SELECTOR, '#user_pass')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[type="submit"]')

    def login(self, username, password):
        self.find_element(self.USERNAME).send_keys(username)
        self.find_element(self.PASSWORD).send_keys(password)
        self.find_element(self.LOGIN_BUTTON).click()

    def get_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
