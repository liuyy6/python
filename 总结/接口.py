#/env/lib/dev python
#--*-- coding:utf-8 -*-
import json
data={'name':'zhang','sex':'man'}
data1=json.dumps(data)  #将字典更改成json数据（字符串）
data2=json.loads(data1)  #将json数据更改为字典
print(data2)
print(type(data2))