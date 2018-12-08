# #接口测试，发送请求，验证是否符合需求的过程
# #postman、jmeter
#
# # #requests  发送http请求    assert  断言处理
# import requests
# import unittest   #python 自带的单元测试，自动化框架
#                     #包含：unittest.TestCase : 测试用例  用来做用例管理，管理测试用例的
#                       #  unittest.TestLoader  ：测试载入，将测试用例，加载到测试套件中
#                       # unittest.TestSuiter  :测试套件，测试集，，将多个测试用例，集合在一起
#                       # unittest.TestRunner  ：执行测试用例
#                       # 封装了检验返回的结果的方法，俗称断言
# class xuexiao():
#     def jiekou(self):
#         # D=input('>>>>')
#         D="北京"
#         url='http://testsupport-be.haofenshu.com/v1/schools/infos'
#         querystring={"filterInput":"{}".format(D)}
#         head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#         'Cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
#         respones=requests.get(url=url,headers=head,params=querystring)
#         html=respones.json()
#         print(html)
#         print(html['msg'])
# #         assert html['code'] == 0  #断言code = 0  ，如果通过无显示    比较落后的方法
# #
# a=xuexiao()
# a.jiekou()




# #练习
# import requests
# import unittest
# class 学校(unittest.TestCase):
#     def setUp(self): # 初始化测试环境  每次执行测试用力前执行，保证每一个用例都在相同环境下执行（提供初始化测试环境）
#         print(123)
#     def test_1(self):    #测试用例，每个测试用例必须以 test 开头
#         print('a')
#     def test_2(self):
#         print('b')
#     def tearDown(self):  # 清理环境，每次用例执行之后，去执行    （善后）
#         print(567)
# unittest.main()    #以test 识别测试用例，执行顺序，按照test_1,后面的在ascll中排序执行
#


#
#实战，自动化测试
# import requests
# import unittest
# class 好分数(unittest.TestCase):
#     def jiekou(self,dm):
#         url='http://testsupport-be.haofenshu.com/v1/schools/infos'
#         querystring={"filterInput":"{}".format(dm)}
#         head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
#                 'Cookie':'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
#         respones=requests.get(url=url,headers=head,params=querystring)
#         json=respones.json()
#         # print(json)






import HTMLTestRunne
import HTMLTestRunnertest
import requests
import unittest
import time
class 考试():
    pass
class 学校(unittest.TestCase):
    def jiekou(self,dm):
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        querystring = {"filterInput": "{}".format(dm)}
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
        respones = requests.get(url=url, headers=head, params=querystring)
        html = respones.json()
        return (html)
    def test_1(self):
        html=self.jiekou('北京')
        self.assertEqual(html['code'],0)
    def test_2(self):
        html=self.jiekou('abcd')
        self.assertNotEqual(html['code'],0)
    def test_3(self):
        html=self.jiekou('北京')
        self.assertEqual(html['data'][0]['schoolName'],'北京七中')
    def test_4(self):
        html=self.jiekou('上海')
        html = self.jiekou('abcd')
        self.assertNotEqual(html['code'], 0)
if __name__ =='__main__':
    # unittest .main()
#
# #生成一个测试套件
    suit=unittest.TestSuite()
#     #添加测试号用例，将测试用例添加到测试套件中
#     suit.addTest(学校('test_1'))   #类的名字（学校），测试用例名（test_1）
#     suit.addTest(学校('test_2'))
#     suit.addTest(学校('test_3'))
#     suit.addTest(学校('test_4'))
    ##############################33
    suit.addTest(unittest.makeSuite(学校))  #将整个类中的所有测试用例，添加到测试套件中
                                            #更具函数名添加的，test
    now=time.strftime('%Y %m %d %H-%M-%S',time.localtime(time.time()))
    with open('abc.html','wb')as f:
        runner=HTMLTestRunnertest.HTMLTestRunner(tester='刘艳颖',
                                                 description='测试结果如下：',
                                                 title='好分数测试报告',
                                                 stream=f)
        runner.run(suit)
        f.close()










