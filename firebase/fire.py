# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 19:01:53 2019

@author: JOE
"""

from firebase import firebase

students=[{"id":'a',"name":"劉軒宏"},
          {"id":'b',"name":"劉軒宏"},
          {"id":'c',"name":"劉軒宏"}]
url='https://linebot-83854.firebaseio.com/'
fb=firebase.FirebaseApplication(url,None)

for student in students:
    fb.post("/students",student)
    print('儲存完畢')
#fb.delete("/students",'')
a=fb.get("/students",'')
b=str(a.values())
b=b.replace('dict_values([{','').replace("'",'').replace(":",'').replace(",",'').replace("}",'').replace("{",'').replace("]",'').replace(")",'').split(" ")
print(b)

