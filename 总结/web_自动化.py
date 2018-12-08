#/usr/bin/env python
#--*-- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains   #动作链
from time import sleep

# dr = webdriver.Firefox()    #打开浏览器
# dr.get('https://www.baidu.com')   #请求的网址
# sleep(1)      #休眠2秒
# print(dr.title)    #获取网站的标题    通常用来做断言
# print(dr.current_url)   #获取网站的网址    通常用作断言

# '#:设计浏览器的大小是为了保证所有的测试用例在同以环境下测试'
# dr.set_window_size(400,400)  #设置浏览器的大小   第一个数字是宽，第二个是高
# sleep(1)      #休眠2秒
# dr.set_window_position(500,400)#设置浏览器产生的位置   第一个：x  第二个：y
# sleep(1)
# dr.maximize_window()  #浏览器最大化
# sleep(2)
# dr.minimize_window()  #浏览器最小化
# sleep(2)      #休眠2秒
# '#浏览器的前进和后退'
# dr.get('http://ifeng.com')
# sleep(1)
# dr.back()  #后退
# sleep(1)
# dr.forward()   #前进
# sleep(1)
"selenium 核心：定位"
'：通过ID定位'
# dr.find_element_by_id('kw').send_keys('我是帅哥')
# sleep(2)
# dr.find_element_by_id('su').click()
# sleep(2)
'通过class属性定位'
# dr.find_element_by_class_name('s_ipt').send_keys('美图')
# sleep(2)
# dr.find_element_by_id('su').click()  #id :定位
# sleep(2)
'通过name属性定位,还有文本定位'
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Chrome()
# dr.get('http://www.moore.ren')
# sleep(2)
# dr.find_element_by_link_text('企业').click()    #通过文本定位
# dr.find_element_by_name('q').send_keys('杭州')   #通过name定位
# dr.find_element_by_id('search-submit').click()
# sleep(5)
# dr.quit()
'通过文本定位'
# from selenium import webdriver
# from time import sleep
# dr=webdriver.Chrome()
# dr.get('http://www.moore.ren')
# sleep(2)
# dr.find_element_by_link_text('企业').click()           #通过文本定位,必须等于文本名
# dr.find_element_by_name('q').send_keys('杭州')
# dr.find_element_by_id('search-submit').click()
# sleep(5)
'模糊的，部分的，通过文本定位'
# dr.get('http://www.moore.ren')
# sleep(2)
# dr.find_element_by_partial_link_text('登').click()  #模糊的，部分的，通过文本定位，只要含有文本中关键字
# sleep(5)
# dr.quit()
'通过标签的名称去定位，通常用于多个元素的定位'
#dr.find_element_by_tag_name('').click()
pass
'通过xpath路径来定位。  xpath：路径标记语言 又叫 xml标记语言'
#                       1、绝对路径( eg：/ html)   2、相对路径 ( // html)
#                       找的是 xml的路径，找xml里的资源
#                       2、xml：可扩展标记语言
#                       xml：1、与html  内容是一模一样的，
#                      3、xml主要作用是传输数据和储存数据，html作用是显示数据
# dr.find_element_by_xpath('/html/body/div[2]/div/div[2]/dl/dd[1]/a').click()  #绝对路径
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()  #相对路径
#
#
'通过css定位'
# dr.get('http://www.moore.ren/login/login.htm')
# sleep(2)
# dr.find_element_by_css_selector('body > div.outerBody > div > div > div > div > div.userRight > div > li:nth-child(2) > a > img').click()
##########################################################################3
# dr=webdriver.Chrome()  #打开浏览器
# dr.get('http://www.moore.ren')  #请求的网址
# wb=dr.find_elements_by_class_name('menu-box')     #定位一组对象
'鼠标循环移动'
# for i in wb:                                       #鼠标循环移动
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(1)
# dr.quit()

# dr=webdriver.Chrome()
# dr.get('https://www.jd.com')
# wb=dr.find_elements_by_class_name('cate_menu_item')
# for i in wb:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(1)
# dr.quit()

'层级定位，先定位大的，然后根据大的定位小的'
# dr=webdriver.Chrome()  #打开浏览器
# dr.get('https://www.jd.com')  #请求的网址
# wb=dr.find_element_by_xpath('//*[@id="J_cate"]/ul') .find_elements_by_tag_name('li')  #层级定位
# print(len(wb))
# dr.quit()

# dr=webdriver.Chrome()  #打开浏览器
# dr.get('http://www.moore.ren')  #请求的网址
# sleep(2)
'获取某元素属性的值     这里获取的是文本'
# wd=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').text
# #print(wd.get_attribute('text'))  #获取某元素属性的值     这里获取的是文本
# print(wd)
# sleep(5)
# dr.quit()


'实战——防火墙'
# dr=webdriver.Chrome()  #打开浏览器
# dr.get('https://192.168.0.254:8889')  #请求的网址   administrator
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# sleep(1)
# wb=dr.find_element_by_css_selector('#checkinfo').find_elements_by_class_name('nobody')
# print(len(wb))
# a=''
# for i in wb:
#     a+=i.get_attribute('src')[-5]
# dr.find_element_by_css_selector('#input1').send_keys(a)
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# sleep(10)
# wd=dr.switch_to_alert() #切换到弹出框
# sleep(2)
# print(wd.text)  #获取弹出框上的文本
# sleep(5)
# dr.quit()
'实战——携程'
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from time import sleep
# import re
# dr=webdriver.Chrome()
# dr.get('http://www.ctrip.com/')
# dr.find_element_by_xpath('//*[@id="J_roomCountList"]').click()
# wb=dr.find_element_by_xpath('//*[@id="J_roomCountList"]').find_elements_by_tag_name('option')
# for j in wb:
#     j.click()
#     sleep(2)


######################################3
'处理窗口'   '每个窗口标号'   '每一个窗口，都给一个唯一的句柄（编号）'
# dr=webdriver.Chrome()  #打开浏览器
# dr.get('http://www.moore.ren')  #请求的网址
# sleep(2)
# print(dr.current_window_handle)#获取当前窗口的句柄
# print(dr.title)
# dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()
# print(dr.current_window_handle)#获取当前窗口的句柄
# wd=dr.window_handles  #获取所有窗口的句柄
# dr.switch_to_window(wd[-1])  #根据句柄切换窗口
# print(dr.title)
# dr.find_element_by_css_selector('#emailInput').send_keys('17839210919')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('lyy17839210919')
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userForm"]/div[2]/div/img').click()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userForm"]/input[1]').click()
# sleep(2)

###############################################
'框架：是镶嵌在web上的一个窗口'    'iFarme :框架'
# dr=webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# wd=dr.find_element_by_xpath('//*[@id="login_frame"]')   # html上面有一个frame
# dr.switch_to.frame(wd)  #切换到内框架   只能根据：id、name、定位到框架来切换
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.switch_to.default_content()   #退出到原始的页面  ，原始页面不是一个框架
# dr.find_element_by_xpath('//*[@id="lay"]/div[3]/div[1]/div[1]/ul/li[1]/a/i').click()  #点击了苹果图标
# #dr.switch_to.parent_frame()   #切换到上一层框架，父框架    ，这里只有一个框架，目前无法实验



########################################################
'弹出框的处理'
dr=webdriver.Chrome()
dr.get('http://192.168.0.254')
sleep(2)
dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
sleep(2)
#弹出框（alert）
wd=dr.switch_to_alert() #切换到弹出框
sleep(2)
print(wd.text)  #获取弹出框上的文本
sleep(100)
wd.accept()  #点击了确定
# # wd.dismiss()  #点击取消
# # wd.send_keys('内容')  #在弹出框输入对应的内容
'实战，喔图云摄影'
# dr=webdriver.Chrome()
# dr.get('http://www.alltuu.com')
# dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]/div/ul/li[6]/div/div/div/a[1]').click()
# dr.find_element_by_xpath('//*[@id="loginUsername"]').send_keys('17839210919')
# sleep(1)
# wd=dr.find_element_by_xpath('/html/body/ul').find_elements_by_tag_name('li')
# for i in wd:
#     if '.com' not in i.text:
#         i.click()
#         sleep(1)
#         dr.find_element_by_xpath('//*[@id="loginPassword"]').send_keys('LYY17839210919')
#         sleep(1)
#         dr.find_element_by_css_selector('#login').click()
#         sleep(1)
#         dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[1]/div/ul/li[6]/div/li/a').click()
#         break
# sleep(1)
# dr.quit()
'实战防火墙'
# dr=webdriver.Chrome()
# dr.get('https:192.168.0.254:8889')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# wd=dr.find_element_by_css_selector('#checkinfo').find_elements_by_tag_name('img')
# a=''
# for i in wd:
#     a+=i.get_attribute('src')[-5]
# dr.find_element_by_css_selector('#input1').send_keys(a)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# wd=dr.switch_to_alert() #切换到弹出框
# sleep(2)
# print(wd.text)  #获取弹出框上的文本
# wd.accept()  #点击了确定
# sleep(10)
# ww=dr.find_element_by_xpath('//*[@id="Content"]/frame[1]')
# dr.switch_to_frame(ww)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="04"]/span[2]').click()
# sleep(1)
# dr.find_element_by_xpath('//*[@id="041"]/span').click()
# sleep(2)
# dr.switch_to_default_content()
# sleep(2)
# dw=dr.find_element_by_xpath('//*[@id="main"]')
# dr.switch_to_frame(dw)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="content"]/form[2]/table/tbody/tr/td[2]/div/div/a').click()
# sleep(2)
# dr.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input').clear()
# dr.find_element_by_xpath('/html/body/form/table[1]/tbody/tr[2]/td/table/tbody/tr[2]/td[4]/input').send_keys('7')
# sleep(2)
# tiao=dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a')
# js="arguments[0].scrollIntoView();"
# dr.execute_script(js,tiao)
# sleep(2)
# dr.find_element_by_xpath('/html/body/form/table[2]/tbody/tr/td/div/div[1]/a').click()
# sleep(5)
# dr.quit()



'滚动条，是属于浏览器的，这一页无法完全显示   滚动条是JavaSciript的一个一个语言'
# dr=webdriver.Chrome()
# dr.get('http://www.alltuu.com')
# sleep(2)
'1.根据页面的高度来移动滚动条'
# js="var q=document.documentElement.scrollTop=1000" #控制滚动条的JavaSciript语言
# #                                1000：表示所有页面的高度；数字越大，滚动条越往下
# a=0
# for i in range(10):
#     print(i)
#     a+=500
#     js="var q=document.documentElement.scrollTop={}".format(a) #控制滚动条的JavaSciript语言
#     #                                1000：表示所有页面的高度；数字越大，滚动条越往下
#     dr.execute_script(js)   #执行JavaSciript 语句
#     sleep(1)
'2.根据定位元素，来移动滚动条'
#    定位一个元素
# wd=dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[4]/div/div[1]/p[1]')
# js="arguments[0].scrollIntoView();"
# dr.execute_script(js,wd)

'鼠标拖拽'
# dr=webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# wd=dr.find_element_by_xpath('//*[@id="login_frame"]')   # html上面有一个frame
# dr.switch_to.frame(wd)  #切换到内框架   只能根据：id、name、定位到框架来切换
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('21223456')
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('qwerty')
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(5)
# wd=dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')   #框架
# dr.switch_to_frame(wd)
# start=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# sleep(5)
# ActionChains(dr).drag_and_drop_by_offset(start,180,0).perform()
# """解释上一句函数：动作链（谁来做）.执行的动作（你要拖动的元素，执行的动作）.开始执行
#                 （                 告诉我你要做什么                      ）.执行这个动作"""

'实战，QQ空间'
# dr=webdriver.Chrome()    #控制浏览器
# dr.get('https://qzone.qq.com')   #打开网址
# w=dr.find_element_by_xpath('//*[@id="login_frame"]')    #定位框架_1
# dr.switch_to_frame(w)    #切换到框架
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()    #点击，账号密码登录
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1873362204')   #输入账号
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('ly545453354')   #输入密码
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()   #确认登录
# print(2)
# sleep(6)
# d=dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')   #定位框架_2
# dr.switch_to_frame(d)   #切换到框架_2
# start=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]/div[1]')   #定位滑块，鼠标
# ActionChains(dr).drag_and_drop_by_offset(start,180,0).perform()     #鼠标按照要求拖拽
# # dr.switch_to_default_content()        #开始 ，横向，纵向
# sleep(5)   #密码错误，自动返回起始框架
# print(dr.title)    #获取网站的标题
# w=dr.find_element_by_xpath('//*[@id="login_frame"]')   #定位框架_1
# dr.switch_to_frame(w)     #切换框架
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('lyy17839210919')   #定位，输入密码
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()   #确认登录
# sleep(5)
# d=dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')    #定位框架_2
# dr.switch_to_frame(d)     #切换框架
# start=dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]/div[1]')  #定位鼠标滑块
# ActionChains(dr).drag_and_drop_by_offset(start,180,0).perform()    #鼠标拖拽，验证
# sleep(5)

#智能等待
import time
import selenium.webdriver.support.ui as ui
dr=webdriver.Chrome()
dr.get('http://www.moore.ren')
dr.minimize_window()
sleep(2)   #强制等待
#智能等待   设置控制器 dr等待

until=ui.WebDriverWait(dr,10)  #  10：最大等待时间     超过时间，报错：timeout
until.until(lambda dr:dr.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_displayed())
'直到你定位的元素显示在屏幕上，就不等待了                                                      显示'
print(time.time())
un=until.until(lambda dr:dr.find_element_by_xpath('//*[@id="user-nomal"]/div[2]/ul/li[2]/a').is_displayed())
print(time.time())
print(un)   #  显示：Ture

'屏幕截图'
dr.get_screenshot_as_file('abc.png')  # 截图并保存     可以更改路径，默认保存在当前

dr.get_screenshot_as_png()           # 截屏
dr.save_screenshot('截图的文件名')    #保存




'函数：'
'is_displayed()  #判断元素是否显示，显示在屏幕上'   #：结果：true   Flase
'is_enabled() #判断元素是否为灰化状态'  #：结果：true   Flase
#  灰化状态:  列如：注册时，不点《同意并接受……》，注册是灰色的，不能点击


