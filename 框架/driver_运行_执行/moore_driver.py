#!/usr/bin/env python
#--*-- coding='utf-8' -*-
from selenium.webdriver.common.action_chains import ActionChains
from 框架.config_配置_公共性.moore_config import moore
from time import sleep
import selenium.webdriver.support.ui as ui
class zidonghua():
    dr=moore().qing()
    until=ui.WebDriverWait(dr,30)
    def web_1(self):
        self.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
        sleep(2)
        a=self.dr.window_handles
        return len(a)
    def web_2(self):
        self.dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[2]/a').click()
        sleep(2)
        a = self.dr.window_handles
        return len(a)
    def web_3(self):
        wb=self.dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[1]/ul/li[1]')
        js="arguments[0].scrollIntoView();"
        self.dr.execute_script(js,wb)
        self.dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[1]/ul/li[1]').click()
        self.dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[2]/ul/li[6]/div[1]/div[2]').click()
        sleep(5)
        wd=self.dr.window_handles
        self.dr.switch_to_window(wd[-1])
        self.dr.find_element_by_css_selector('body > div.main > div > div > div.content-left.content-left2 > div.company-detail > div.top-title > div > a > span > div > span').click()
        sleep(5)
        self.dr.find_element_by_xpath('//*[@id="needlogin_favorite"]/div/a').click()
        sleep(5)
        aa=self.dr.find_element_by_class_name('input-listener').is_displayed()
        print(aa)
        try:
            a=self.dr.find_element_by_class_name('input-listener').text
        except:
            a='1234'
        print(a)





a=zidonghua()
a.web_3()