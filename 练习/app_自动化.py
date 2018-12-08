#！/usr/lib/env python
#--*-- coding=utf-8 -*-
from appium import webdriver
import time
import unittest
import HTMLTestRunnertest
import selenium.webdriver.support.ui as ui
class aap_1(unittest.TestCase):
    def config(self):
        desired_caps = {'platformName': 'Android',
                        #  'platformVersion':'5.0',      #版本号错误
                        'deviceName': '127.0.0.1:62001',
                        'appPackage': 'com.netease.cloudmusic',
                        'appActivity': 'activity.LoadingActivity'}
        """平台机，类型
        设备版本      可以不写，新版的 appium 可以不写
        设备名称
        activity值：测试安装包的activity值
        """
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 开启 appium 服务器
        '                        appium 服务器地址  建立连接  ， 告诉服务器基本信息'
        # driver.quit()
        # time.sleep(20)
        return driver
    def drvice_1(self):
        driver = self.config()
        until=ui.WebDriverWait(driver,20)
        print('立即体验')
        until.until(lambda driver:driver.find_element_by_id('com.netease.cloudmusic:id/mx').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/mx').click()
        print('列表')
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/py').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
        print('登录')
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/abx').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/abx').click()
        print('手机号登录')
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/aih').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/aih').click()
        print('手机号')
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/i1').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/i1').send_keys('17839210919@163.com')
        time.sleep(1)
        print('密码')
        driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('LYY17839210919')
        time.sleep(1)
        print('登录')
        driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
        until.until(lambda driver:driver.find_element_by_id('com.netease.cloudmusic:id/py').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/ac2').is_displayed())
        aa=driver.find_element_by_id('com.netease.cloudmusic:id/ac2').text
        time.sleep(1)
        driver.quit()
        return aa
    def drvice_2(self):
        driver = self.config()
        until = ui.WebDriverWait(driver, 20)
        print('立即体验')
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/mx').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/mx').click()
        print('列表')
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/py').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
        print('登录')
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/abx').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/abx').click()
        print('手机号登录')
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/aih').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/aih').click()
        print('手机号')
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/i1').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/i1').send_keys('17839210919@163.com')
        time.sleep(1)
        print('密码')
        driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('LYY17839210919')
        time.sleep(1)
        print('登录')
        driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/aam').is_displayed())
        driver.find_element_by_id('com.netease.cloudmusic:id/aam').click()
        until.until(lambda driver: driver.find_element_by_id('com.netease.cloudmusic:id/adm').is_displayed())
        aa=driver.find_element_by_id('com.netease.cloudmusic:id/adm').text
        driver.quit()
        return aa
    def test_1(self):
        aa=self.drvice_1()
        self.assertEqual(aa,'我是你的_影')
    def test_2(self):
        aa=self.drvice_2()
        self.assertEqual(aa,'官方榜')


if __name__=='__main__':
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(unittest.makeSuite(aap_1))  # 将整个类中的所有测试用例，添加到测试套件中
    # 更具函数名添加的，test
    now = time.strftime('%Y %m %d %H-%M-%S', time.localtime(time.time()))
    with open('app.html', 'wb')as f:
        runner = HTMLTestRunnertest.HTMLTestRunner(tester='刘艳颖',
                                                   description='测试结果如下：',
                                                   title='网易云音乐',
                                                   stream=f)
        runner.run(suit)
        f.close()


