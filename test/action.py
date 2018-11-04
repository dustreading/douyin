import time

from test import CAP
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Remote("http://localhost:4723/wd/hub", CAP)


def click_s(x, y):
    while True:
        if "首页" in driver.page_source:
            driver.tap([(x, y)])
            break


def click_i(x, y):
    while True:
        if "推荐" in driver.page_source:
            driver.tap([(x, y)])
            break


def send(msg, to):
    # driver.find_element_by_id(to).send_keys(msg)
    # if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath(to)):
    #     driver.find_element_by_xpath(to).send_keys(msg)
    driver.find_element_by_xpath(to).send_keys(msg)

def click_sx(to):
    driver.find_element_by_xpath(to).click()