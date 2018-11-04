from test.action import click_s, send, click_i, click_sx, driver
from test import *

click_s(*SEARCH)
driver.find_element_by_id(SEARCH_BAR_ID).send_keys("ig")
driver.find_element_by_id(SEARCH_ID).click()

# send("ig", INPUT_X)
# click_sx(SEARCH_X)
