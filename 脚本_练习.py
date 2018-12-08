#！/usr/lib/env python
#--*-- coding=utf-8 -*-
# import requests
# # import re
# # import pymysql
# # class Boss():
# #     def qing(self):
# #         url='https://www.zhipin.com/c101010100-p100309'
# #         head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
# #         'referer': 'https: // www.zhipin.com / c101010100 - p100309 '}
# #         res=requests.get(url=url,headers=head)
# #         html=res.content.decode('utf-8')
# #         return html
# #     def guolv(self,html):
# #         patt=re.compile('<div class="job-title">(.*?)</div>',re.S)
# #         zhiwei=patt.findall(html)
# #         print(len(zhiwei))
# #         patt_1=re.compile(' <div class="info-primary">(.*?)</li>',re.S)
# #         itmes=patt_1.findall(html)
# #         gongsi=[]
# #         xinzi=[]
# #         didian=[]
# #         jingyan=[]
# #         patt_2=re.compile('<span class="red">(.*?)</span>',re.S)
# #         patt_3=re.compile('<div class="info-detail"></div>(.*?)</div>',re.S)
# #         for i in itmes:
# #             xinzi.append(patt_2.findall(i)[0])
# #             di=patt_3.findall(i)
# #             patt_3_2=re.compile('<p>(.*?)<em',re.S)
# #             didian.append(patt_3_2.findall(di[0])[0])
# #             patt_4=re.compile('<em class="vline"></em>(.*?)<em class="vline"></em>',re.S)
# #             jingyan.append(patt_4.findall(di[0])[0])
# #             patt_5=re.compile('<div class="company-text">(.*?)</h3>',re.S)
# #             si=patt_5.findall(i)
# #             patt_5_5=re.compile('target="_blank">(.*?)</a>',re.S)
# #             gongsi.append(patt_5_5.findall(si[0])[0])
# #         print(len(didian))
# #         print(len(xinzi))
# #         print(len(jingyan))
# #         print(len(gongsi))
# #         a=list(zip(gongsi,zhiwei,xinzi,didian,jingyan))
# #         return a
# # a=Boss()
# # html=a.qing()
# # shuju=a.guolv(html)
# # # print(shuju)
# #
# #
# # abc=pymysql.connect(host='192.168.0.187',
# #                     port=3306,
# #                     user='root',
# #                     password='686789',
# #                     charset='utf8')
# # a=abc.cursor()
# # a.execute('use py')
# # a.execute('show tables')
# # # print(a.fetchall())
# # # a.execute('create table Boos(公司 char(50),职位 char(50),薪资 char(50),工作地点 char(50),经验 char(50))')
# # a.execute('desc Boos')
# # # print(a.fetchall())
# # for i in range(len(shuju)):
# #     a.execute('insert into Boos values("{}","{}","{}","{}","{}")'.format(shuju[i][0],shuju[i][1],shuju[i][2],shuju[i][3],shuju[i][4]))
# # a.execute('select * from Boos')
# # print(a.fetchall())
#
# ##################################
# # import unittest
# # from selenium import webdriver
# # from time import sleep
# # from selenium.webdriver.common.action_chains import ActionChains
# # import selenium.webdriver.support.ui as ui
# # class qq(unittest.TestCase):
# #     def qing(self):
# #         dr=webdriver.Chrome()
# #         dr.get('https://qzone.qq.com')
# #         wd=dr.find_element_by_xpath('//*[@id="login_frame"]')
# #         dr.switch_to_frame(wd)
# #         dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# #         b=dr.title
# #         sleep(2)
# #         dr.find_element_by_xpath('//*[@id="u"]').send_keys('12345678')
# #         dr.find_element_by_xpath('//*[@id="p"]').send_keys('wertyudfgh')
# #         sleep(2)
# #         dr.find_element_by_xpath('//*[@id="login_button"]').click()
# #         until=ui.WebDriverWait(dr,30)
# #         until.until(lambda dr:dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe').is_displayed())
# #         ww=dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# #         dr.switch_to_frame(ww)
# #         while True:
# #             try:
# #                 start=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# #                 ActionChains(dr).drag_and_drop_by_offset(start,180,0).perform()
# #                 sleep(2)
# #             except:
# #                 break
# #         sleep(5)
# #         dr.switch_to_frame(wd)
# #         dr.find_element_by_xpath('//*[@id="u"]').clear()
# #         dr.find_element_by_xpath('//*[@id="p"]').clear()
# #         dr.find_element_by_xpath('//*[@id="u"]').send_keys('1873362204')
# #         sleep(1)
# #         dr.find_element_by_xpath('//*[@id="p"]').send_keys('lyy17839210919')
# #         sleep(2)
# #         dr.find_element_by_xpath('//*[@id="login_button"]').click()
# #         until=ui.WebDriverWait(dr,30)
# #         until.until(lambda dr:dr.find_element_by_xpath('//*[@id="QZ_Shop_Items_Container"]/div[1]/div/div/ul/li[3]/a').is_displayed())
# #         a=dr.title
# #         print(a)
# #         # sleep(10)
# #         return a
# #     def test(self):
# #         a=self.qing()
# #         self.assertEqual(a,'精灵 [http://1873362204.qzone.qq.com]')
# # if __name__=='__main__':
# #     unittest.main()



#！/usr/bin/env python
#--*--coding:utf-8 -*-
# from selenium import webdriver
# # from selenium.webdriver.common.action_chains import ActionChains
# # from time import sleep
# # import selenium.webdriver.support.ui as ui
# # dr=webdriver.Chrome()
# # dr.get('https://www.jd.com')
# # until=ui.WebDriverWait(dr,22)
# # until.until(lambda dr:dr.find_element_by_xpath('//*[@id="key"]').is_displayed())
# # dr.find_element_by_class_name('link-login').click()
# # until.until(lambda dr:dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').is_displayed())
# # dr.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[3]/a').click()
# # dr.find_element_by_id('loginname').send_keys('17839210919')
# # dr.find_element_by_id('nloginpwd').send_keys('LYY17839210919')
# # sleep(1)
# # dr.find_element_by_xpath('//*[@id="loginsubmit"]').click()
# # until.until(lambda dr:dr.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]').is_displayed())
# # while True:
# #     try:
# #         start = dr.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]')
# #         ActionChains(dr).drag_and_drop_by_offset(start, 64, 0).perform()
# #         sleep(10)
# #     except:
# #         break
# # until.until(lambda dr:dr.find_element_by_xpath('//*[@id="key"]').is_displayed())
# # dr.find_element_by_xpath('//*[@id="key"]').send_keys('电脑')





#/usr/bin/env python
#--*--  coding='utf-8' -*-



