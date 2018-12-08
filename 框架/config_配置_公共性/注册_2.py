#!/usr/lib/env python
#--*--coding=utf-8 -*-
import requests
class qing():
    def qi(self,dell,password):
        url='http://www.zhaoapi.cn/user/reg'
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'}
        payload='mobile={}&password={}'.format(dell,password)
        # print(payload)
        res=requests.request('POST',url=url,headers=head,data=payload)
        json=res.json()
        return json
a=qing()
a.qi(13855223657,1234567)