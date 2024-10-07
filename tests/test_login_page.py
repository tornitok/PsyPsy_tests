import pytest

def test_success_log_in(login_page):
    login_page.enter_user_name()
    login_page.enter_password()
    login_page.click_button()
    login_page.is_url_valid()


@pytest.mark.parametrize(
    'user_name, password, error_message',
    [
        ('tomsmith@mail.com', '123456', 'Неверное имя пользователя или пароль.'),
        ('', '123456', 'Поле E-Mail адрес обязательно для заполнения.'),
        ('test@ts.ts', '', 'Неверное имя пользователя или пароль.'),
        ('', '', 'Поле E-Mail адрес обязательно для заполнения.'),
    ],
    ids=[
        'invalid_credentials',
        'empty_user_name',
        'empty_password',
        'empty_fields'
    ]
)
def test_unsuccessful_log_in(login_page, user_name, password, error_message):
    login_page.enter_user_name(user_name)
    login_page.enter_password(password)
    login_page.click_button()
    login_page.is_error_message_correct(error_message)