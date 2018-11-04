from app import *
from app.action import click, insert, slip

# 基于"夜神模拟器Android 5.1.1"和"抖音2.8.0"
click(SEARCH_ICON)
insert(SEARCH_INSERT, 274110380)
click(SEARCH)
click(HEAD)
click(FANS)
slip()
