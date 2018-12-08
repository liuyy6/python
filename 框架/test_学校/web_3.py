#!/usr/lib/env  python
#--*-- coding=utf-8  -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from 框架.config_配置_公共性.wed_1 import deng
import unittest
import selenium.webdriver.support.ui as ui
from time import sleep
class yong(unittest.TestCase):
    def test_1_登录(self):
        dr = deng().denglu()
        dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
        sleep(5)
        wd = dr.window_handles
        dr.switch_to_window(wd[-1])
        until = ui.WebDriverWait(dr, 10)
        un = until.until(lambda dr: dr.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div/div[1]/form/input[1]').is_displayed())
        self.assertTrue(un)
        dr.quit()

    def test_2_注册(self):
        dr = deng().denglu()
        dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/div[1]/li[2]/a').click()
        sleep(5)
        wd = dr.window_handles
        dr.switch_to_window(wd[-1])
        until = ui.WebDriverWait(dr, 10)
        un = until.until(lambda dr: dr.find_element_by_xpath(
            '/html/body/div[2]/div/div/div/div[1]/div[1]/div[2]/form/input[2]').is_displayed())
        self.assertTrue(un)
        dr.quit()

    def test_3_热门职位(self):
        dr = deng().denglu()
        wd = dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[1]/ul/li[1]')
        js = "arguments[0].scrollIntoView();"
        dr.execute_script(js, wd)
        dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[1]/ul/li[1]').click()
        aa = dr.find_element_by_xpath('/html/body/div[2]/div/div[4]/div[1]/div[1]/ul/li[1]').text
        self.assertTrue('热门职位',aa)
        dr.find_element_by_css_selector(
            'html.js.flexbox.canvas.canvastext.webgl.no-touch.geolocation.postmessage.no-websqldatabase.indexeddb.hashchange.history.draganddrop.websockets.rgba.hsla.multiplebgs.backgroundsize.borderimage.borderradius.boxshadow.textshadow.opacity.cssanimations.csscolumns.cssgradients.no-cssreflections.csstransforms.csstransforms3d.csstransitions.fontface.generatedcontent.video.audio.localstorage.sessionstorage.webworkers.no-applicationcache.svg.inlinesvg.smil.svgclippaths body div.main div.wrap div.main_bottom div.job-list-main div.job-list ul.job-for-you li.job-list-item div.job-list-top div.clearfix').click()
        sleep(5)
        wdq = dr.window_handles
        dr.switch_to_window(wdq[-1])
        until=ui.WebDriverWait(dr,10)
        until.until(lambda dr:dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/a/span/div/span').is_displayed())
        dd = dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/a/span/div/span').text
        # print(dd)
        dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/a/span/div/span').click()
        self.assertEqual('收藏职位',dd)
        until = ui.WebDriverWait(dr,10)
        until.until(lambda dr: dr.find_element_by_xpath('/html/body/div[21]/div[1]/div[2]/div[2]/div[1]/div/div/a').is_displayed())
        aaa = dr.find_element_by_xpath('/html/body/div[21]/div[1]/div[2]/div[2]/div[1]/div/div/a').text
        dr.find_element_by_xpath('/html/body/div[21]/div[1]/div[2]/div[2]/div[1]/div/div/a').click()
        # print(aaa)
        self.assertEqual('立即登录',aaa)
        dr.quit()
    def test_4_一件投递(self):
        dr=deng().denglu()
        dr.get('http://www.moore.ren/job/detail.htm?jobId=1211953')
        wd=dr.window_handles
        dr.switch_to_window(wd[-1])
        ulit=ui.WebDriverWait(dr,10)
        ulit.until(lambda dr:dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[3]/a').is_displayed())
        dr.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div[1]/div[3]/a').click()
        sleep(1)
        dr.find_element_by_xpath('/html/body/div[21]/div[1]/div[2]/div[2]/div[1]/div/div/div[1]').click()


# a=yong()
# a.test_3_热门职位()
if __name__ =='__main__':
    unittest.main()
# suit = unittest.TestSuite()
# #     #     #添加测试号用例，将测试用例添加到测试套件中
#     suit.addTest(yong('test_热门职位'))   #类的名字（学校），测试用例名（test_1）