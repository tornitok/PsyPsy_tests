from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
BASE_URL = 'https://psy@admin.com:psy@admin.com@24psypsy.ru/profile/'
web_driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
login = 'bipixoj940@ploncy.com'
password = 'bipixoj940@ploncy.com'

def wait_for_element(driver, by, value, timeout=3):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located((by, value)))

def test_chat():
    web_driver.get(url=BASE_URL)
    login_field = web_driver.find_element(By.CSS_SELECTOR, '#user_login')
    password_field = web_driver.find_element(By.CSS_SELECTOR, '#user_pass')
    login_buj
    wait = WebDriverWait(web_driver, 5)
    login_field.send_keys(login)
    l

