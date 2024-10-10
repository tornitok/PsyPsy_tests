from typing import Final
from dotenv import load_dotenv
import os

load_dotenv()


class Secrets:
    USER_NAME_CLIENT: Final[str] = os.getenv('USER_NAME_CLIENT')
    PASSWORD_CLIENT: Final[str] = os.getenv('PASSWORD_CLIENT')

class URL:
    BASE_URL = 'https://psy@admin.com:psy@admin.com@24psypsy.ru'
    INDEX_PAGE = f'{BASE_URL}/auth'
    PROFILE_PAGE = f'{BASE_URL}/profile/'
