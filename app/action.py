import time

from app import CAP
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Remote("http://localhost:4723/wd/hub", CAP)


def get_window():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def click(xpath):
    try:
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath)):
            driver.find_element_by_xpath(xpath).click()
    except:
        pass


def insert(xpath, content):
    try:
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(xpath)):
            driver.find_element_by_xpath(xpath).send_keys(content)
    except:
        pass


def slip(direction=1):
    x = get_window()[0] * 0.5
    y1 = get_window()[1] * 0.75
    y2 = get_window()[1] * 0.25
    while True:
        if '没有更多了' in driver.page_source:
            break
        if direction == 0:
            driver.swipe(x, y2, x, y1)
            time.sleep(1)
        else:
            driver.swipe(x, y1, x, y2)
