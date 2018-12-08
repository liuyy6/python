#！/usr/bin/env python
#--*-- coding:utf-8
import requests
class 学校_查询():
    def 学校_快查(self,d):
        url = 'http://testsupport-be.haofenshu.com/v1/schools/infos'
        querystring = {"filterInput": "{}".format(d)}
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
        respones = requests.get(url=url, headers=head, params=querystring)
        html = respones.json()
        return (html)