#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-06 10:29
# @Author  : Aries
# @Site    : 
# @File    : develop_model.py
# @Software: PyCharm
#对网页的一些操作函数，登录，查询，校对


from selenium import webdriver
from time import sleep
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By


class model():


    #登录
    def login(driver,name,pwd):
        try:
            ele_loginname = WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.ID,"")))
            ele_loginpwd = WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.ID, "")))
            ele_login = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, "")))
            ele_loginname.send_keys(name)
            ele_loginpwd.send_keys(pwd)
            sleep(3)
            ele_login.click()
            sleep(5)
        except TimeoutException as e:
            print(" login failled !!!")
            print(e)

    #搜索
    def search(driver,key):
        try:
            ele_search_input = WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.ID,"")))
            ele_search_input.send_key(key)
            ele_search = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.ID, "")))
            ele_search.click()
        except TimeoutException as e:
            print("search failled !!!")
            print(e)

     #校验
    def reasult_assert(driver,expected,actual):
        try:
            ele_actual = WebDriverWait(driver,10,1).until(EC.presence_of_element_located((By.ID,actual)))
            if ele_actual == expected:
                print("搜索成功")
                return True
            else:
                print("搜索失败！！！")
                return False

        except TimeoutException as e:
            print("search failled !!!")
            print(e)




