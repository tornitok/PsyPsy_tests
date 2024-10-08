from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import urllib.parse

class BaseObject:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def _is_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def _is_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator))

    def find_element(self, locator: tuple[str, str], time=10) -> WebElement:
        return WebDriverWait(
            self.driver, time).until(ec.presence_of_element_located(locator))

    def click(self,locator: tuple[str, str]) -> None:
        self._is_clickable(locator).click()

    def send_keys(self, locator: tuple[str, str], value: str) -> None:
        self._is_visible(locator).send_keys(value)

    def get_current_url(self) -> str:
        return urllib.parse.unquote(self.driver.current_url)

    def get_text(self, locator:tuple[str, str]) -> str:
        return self._is_visible(locator).text

    def get_file(self, locator:tuple[str, str]) -> WebElement:
        return self._is_visible(locator)