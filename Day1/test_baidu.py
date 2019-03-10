#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-03 15:38
# @Author  : kuxui
# @Site    : 
# @File    : test_baidu.py
# @Software: PyCharm


from selenium import webdriver
from time import sleep


# 启动Chrome浏览器
driver = webdriver.Chrome()

# 打开百度页面
driver.get("https://www.baidu.com/")

# 等待3秒
sleep(3)

# 关闭浏览器
driver.quit()