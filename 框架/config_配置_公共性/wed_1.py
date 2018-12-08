#!/usr/lib/env  python
#--*-- coding=utf-8  -*-
from selenium import webdriver
from time import sleep
class deng():
    def denglu(self):
        dr=webdriver.Firefox()
        dr.get('http://www.moore.ren')
        #dr.minimize_window()
        return dr
