#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-07 14:16
# @Author  : Aries
# @Site    : 
# @File    : read_file.py
# @Software: PyCharm
#用于读取文件，text，Excel，xml
#xlrd模块读取excel文件，xlwt模块用来写Excel（两个模块属于第三方模块需要安装）
from xml.dom import minidom
import xml.etree.ElementTree as ET
import xlrd
from xml.dom.minidom import parse



class readfile():

    # path = "/Users/superkoxui/PycharmProjects/myfirst_auto_ui/Day5/data"
    # path = "/Users/superkoxui/PycharmProjects/myfirst_auto_ui/Day5/dataexcel.xlsx"
    path = "/Users/superkoxui/PycharmProjects/myfirst_auto_ui/Day5/data_values"
    #读取text
    def readtext(path):
        data = []
        with open(path,'r') as f:
            print("open file sucess !!!")
            line = f.readline()
            while line:
                data.append(line.strip("\n"))
                line = f.readline()
        return data

    #读取Excel
    def readexcel(path):
        data = []
        workbook = xlrd.open_workbook(path)
        #通过名字获取sheet页
        sheet = workbook.sheet_by_name("num1")
        nrows = sheet.nrows #行
        ncols = sheet.ncols #列
        for i in range(nrows):
            data.append(sheet.cell_value(i,0))
        return data

    #读取xml
    def readxml(path):
        data = []
        dom = ET.parse(path)
        # root = dom.documentElement
        node = dom.find('./首页')
        print(type(node))




    datas = readxml(path)























