from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest

login = 'bipixoj940@ploncy.com'
password = 'bipixoj940@ploncy.com'
timeout = 5

@pytest.fixture
def login_page(browser):
    login_page = LoginPage(browser)
    login_page.open('/auth')
    return login_page

def wait_for_element(browser, locator, timeout=timeout):
    wait = WebDriverWait(browser, timeout)
    return wait.until(EC.visibility_of_element_located(locator))

def test_successful_login(browser, login_page):
    login_page.login(login, password)
    dashboard_element = wait_for_element(browser, (By.CLASS_NAME, 'psy-chat'))
    assert dashboard_element is not None, "Login failed - not redirected to dashboard"

def test_failed_login(browser, login_page):
    login_page.login('tomsmith@mail.com', 'wrongpassword')
    error_message = login_page.get_error_message()
    assert 'Неверное имя пользователя или пароль.' in error_message, 'Отсутствует ошибка'