from time import sleep

import pytest

def test_send_message(chat_page):
    chat_page.log_in()
    chat_page.enter_message('Test message')
    chat_page.send_message()

def test_send_urgent_message(chat_page):
    chat_page.log_in()
    chat_page.enter_message('Test urgent message')
    chat_page.set_urgent_flag()
    chat_page.send_message()
#
# def wait_for_element(browser, locator, timeout=TIMEOUT):
#     wait = WebDriverWait(browser, timeout)
#     return wait.until(EC.visibility_of_element_located(locator))
#
# def test_chat_text(browser, chat_page):
#     message = 'Тестовый текст'
#     chat_page.send_message(message)
#     sent_message = wait_for_element(browser, (By.CSS_SELECTOR, '.sent:last-child .content_text span'))
#     assert sent_message.text == message, 'Сообщение не отправлено'
#
# def test_chat_urgent_text(browser, chat_page):
#     chat_page = ChatPage(browser)
#     message = 'Тестовый срочный текст'
#     chat_page.send_urgent_message(message)
#     sent_message = wait_for_element(browser, (By.CSS_SELECTOR, '.urgent:last-child .content_text span'))
#     assert sent_message.text == message, 'Срочное сообщение не отправлено'
#
# def test_chat_send_file(browser, login_page):
#     pass
