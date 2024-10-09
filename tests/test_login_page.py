import pytest

def test_success_log_in(login_page):
    login_page.enter_email()
    login_page.enter_password()
    login_page.click_button()
    login_page.is_url_valid()


@pytest.mark.parametrize(
    'user_name, password, error_message',
    [
        ('tomsmith@mail.com', '123456', 'Неверное имя пользователя или пароль.'),
        ('', '123456', 'Поле E-Mail адрес обязательно для заполнения.'),
        ('tomsmith@mail.com', '', 'Неверное имя пользователя или пароль.'),
        ('', '', 'Поле E-Mail адрес обязательно для заполнения.'),
        ('123@ts.ts', '', 'Поле E-Mail адрес должно быть действительным электронным адресом.')
    ],
    ids=[
        'invalid_credentials',
        'empty_email',
        'empty_password',
        'empty_fields',
        'non_existent_email'
    ]
)
def test_unsuccessful_log_in(login_page, user_name, password, error_message):
    login_page.enter_user_name(user_name)
    login_page.enter_password(password)
    login_page.click_button()
    login_page.is_error_message_correct(error_message)