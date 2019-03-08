#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-02-14 10:40
# @Author  : kuxui
# @Site    : 
# @File    : les2_positioning.py
# @Software: PyCharm
# 功能：用多种方式定位京东登录页元素：id定位、nane定位、class name定位、tag name定位、linke text定位、
#                              partial link text定位、xpath定位、css定位

from selenium import webdriver
from time import sleep


# 清空用户名&密码输入框
def clear():
    driver.find_element_by_id("loginname").clear()
    driver.find_element_by_id("nloginpwd").clear()


# 1.启动浏览器
driver = webdriver.Chrome()
# 2.打开京东网页
driver.get("https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F")
# 3.扫码登录和账户登录，选择账户登录
driver.find_element_by_link_text("账户登录").click()

# HTML元素定位，定位用户名并输入值，定位密码并输入值
# 1>id定位
# sleep(2)
# driver.find_element_by_id("loginname").send_keys("loginname")
# sleep(2)
# driver.find_element_by_id("nloginpwd").send_keys("nloginpwd")
# sleep(2)
# # 2>nane定位
# clear()
# sleep(2)
# driver.find_element_by_name("loginname").send_keys("loginname")
# sleep(2)
# driver.find_element_by_name("nloginpwd").send_keys("nloginpwd")
# sleep(2)
# # 3>class name定位
# clear()
# sleep(2)
# driver.find_element_by_class_name("itxt").send_keys("itxt")
# sleep(2)
# driver.find_element_by_class_name("itxt-error").send_keys("itxt-error")
# sleep(2)
# 4>tag name定位
# clear()
# sleep(2)
# driver.find_elements_by_tag_name("input")[10].send_keys("10")
# sleep(2)
# driver.find_elements_by_tag_name("input")[11].send_keys("10")
# sleep(2)
# 5>linke text定位"忘记密码"
# clear()
# sleep(2)
# driver.find_element_by_link_text("忘记密码").click()
# 6>partial link text定位   截取文本其中一部分定位
# clear()
# sleep(2)
# driver.find_element_by_partial_link_text("忘记").click()
# sleep(2)
# 7>xpath定位  绝对路径定位、相对路径定位、绝对路径加元素属性定位（属性的值一定要写全部的值）、xpath逻辑运算符定位
clear()
sleep(2)
driver.find_element_by_xpath("//div[@class='item item-fore1' ]/input").send_keys("绝对路径钾元素class属性")
sleep(2)
driver.find_element_by_xpath("//div[@id='entry' ]/input").send_keys("绝对路径钾元素id属性")
sleep(2)
# 8>css定位


# 等3秒
sleep(3)
# 关闭浏览器
driver.quit()