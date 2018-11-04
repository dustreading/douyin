from multiprocess import *
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


def start(ip, cap, msg):
    driver = webdriver.Remote(ip, cap)
    click(driver, ENTRANCE, "首页")
    while True:
        loop(driver, msg)


def loop(driver, msg):
    insert(driver, msg, INPUT_ID)
    click_id(driver, SEARCH_ID)
    click_id(driver, NAME_ID)
    click_id(driver, FANS_ID)
    swipe(driver, "TA的粉丝", "没有更多了", "没有粉丝")
    click(driver, BACK)
    click(driver, BACK)


def get_window(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


def click(driver, pos, ident=""):
    while True:
        if ident in driver.page_source:
            driver.tap([pos])
            break


def click_id(driver, element):
    while True:
        try:
            driver.find_element_by_id(element).click()
            break
        except NoSuchElementException:
            pass


def insert(driver, msg, element):
    while True:
        try:
            driver.find_element_by_id(element).send_keys(msg)
            break
        except NoSuchElementException:
            pass


def swipe(driver, ident, *kwargs):
    x, y = get_window(driver)
    while True:
        if ident in driver.page_source:
            driver.swipe(x*0.5, y*0.75, x*0.5, y*0.25)
        flag = 0
        for arg in kwargs:
            if arg in driver.page_source:
                flag = 1
                break
        if flag == 1:
            break
