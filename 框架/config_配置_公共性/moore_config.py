#！/usr/bin/env python
#--*-- coding:utf-8
from selenium import webdriver
from time import sleep
class moore():
    def qing(self):
        dr=webdriver.Chrome()
        dr.get('http://www.moore.ren')
        return dr