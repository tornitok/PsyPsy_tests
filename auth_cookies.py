import json
import datetime
from collections import ChainMap
import os

FULL_PATH = os.path.dirname(os.path.realpath(__file__))
COOKIE_PATH = FULL_PATH + '/cookies.json'


def get_app_cookies(driver, url):
    driver.get(url)
    # authorization steps here
    new_cookies = driver.get_cookie("XSRF-TOKEN") # replace cookie_name with your cookie name
    new_value = new_cookies["value"]
    expiry_date = new_cookies["expiry"]

    with open(COOKIE_PATH, "r") as f:
        data1 = json.load(f)
    for d in data1:
        d.update((k, new_value) for k, v in d.items() if k == "value")
    for d in data1:
        d.update((k, expiry_date) for k, v in d.items() if k == "expiry")

    with open(COOKIE_PATH, "w") as f:
        json.dump(data1, f)


def load_app_cookies(driver, url):
    cookies = json.load(open(COOKIE_PATH, "rb"))
    driver.execute_cdp_cmd('Network.enable', {})
    for cookie in cookies:
        if "expiry" in cookie:
            cookie["expires"] = cookie["expiry"]
            del cookie["expiry"]
        cookie["domain"] = cookie["domain"]
        driver.execute_cdp_cmd('Network.setCookie', cookie)
    driver.execute_cdp_cmd('Network.disable', {})
    driver.get(url)


def execute_cookies(driver, url):
    with open(COOKIE_PATH, "r") as f:
        data1 = json.load(f)
    data2 = dict(ChainMap(*data1))
    print(data2)
    today_date = datetime.date.today()
    print(data2["expiry"])
    epoch_time = data2["expiry"]
    new_date = datetime.datetime.fromtimestamp(epoch_time).date()
    if today_date < new_date:
        load_app_cookies(driver, url)
    elif today_date >= new_date:
        get_app_cookies(driver, url)