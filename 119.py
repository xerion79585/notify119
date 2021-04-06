# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 22:07:12 2021

@author: user
"""

from bs4 import BeautifulSoup
import requests
from firebase import firebase
import time

A=[]

while 1:
  Q=[]
  Token=[]
  try:
    
    url='https://hihi-20070-default-rtdb.firebaseio.com/'
    fb=firebase.FirebaseApplication(url,None)
    
    clean=fb.get("/clean",'')
    
    if clean!=None:
        A=[]
        fb.delete('/clean','')
    
    
    
    up=fb.get("/up",'')
    up=str(up).split(',')
 
    up=str(up).split(':')[1].replace('}','').replace(' ','').replace("'",'').replace("]",'').replace('"','')
    time.sleep(int(up))
    token=fb.get("/token",'')
    token=str(token).split(',')
 
    
    
    
    
    
    
    
    B=fb.get("/hi",'')
    B=str(B).split(',')
    for i in range(0,len(B)):
        Q=Q+[B[i].replace("'",'').replace("}",'').replace("關鍵字:",'').replace(" ",'').split(':')[1]]
    for i in range(0,len(token)):
        Token=Token+[token[i].replace("'",'').replace("}",'').replace("關鍵字:",'').replace(" ",'').split(':')[1]]
    
    url= 'http://210.241.127.68:8080/DTS/caselist/html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    ' AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/70.0.3538.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    bs = BeautifulSoup(response.text, 'lxml')
    bs = str(bs)
    bs=bs.split('</tr>')
    for i in range(1,len(bs)-7):
        a=bs[i].replace('td','').replace('td','').replace('<','').replace('>','').replace('\n',' ').replace('/','').replace('!','').replace('tr','').replace('-','').replace('\r','')
        for j in range(0,len(Q)):
            
            if '&' not in Q[j]: 
            
                if Q[j] in a:
                    
                    ans='\n'+a.split(' ')[5][0:4]+'/'+a.split(' ')[5][4:6]+'/'+a.split(' ')[5][6:]+' '+a.split(' ')[6]+'\n'+a.split(' ')[7]+'/'+a.split(' ')[8]+'\n'+a.split(' ')[9]+'\n'+a.split(' ')[10]+'\n'+a.split(' ')[11]
                    if ans not in A:    
                        print(ans)
                        A=A+[ans]
                        for l in range(0,len(Token)):
                            headers = {
                                    "Authorization": "Bearer " + Token[l],
                                    "Content-Type": "application/x-www-form-urlencoded"
                                }
                            
                            params = {"message": ans}
                             
                            r = requests.post("https://notify-api.line.me/api/notify",
                                              headers=headers, params=params)
                            
                            print(r.status_code)
                    
            else:
                E=0
                QQ=Q[j].split('&')
                
                for k in range(0,len(QQ)):
                    if QQ[k] in a:
                        E=E+1
                        
                if E==len(QQ):
                    ans='\n'+a.split(' ')[5][0:4]+'/'+a.split(' ')[5][4:6]+'/'+a.split(' ')[5][6:]+' '+a.split(' ')[6]+'\n'+a.split(' ')[7]+'/'+a.split(' ')[8]+'\n'+a.split(' ')[9]+'\n'+a.split(' ')[10]+'\n'+a.split(' ')[11]
                    if ans not in A:    
                     #   print(ans)
                        A=A+[ans]
                        for l in range(0,len(Token)):
                            headers = {
                                    "Authorization": "Bearer " + Token[l],
                                    "Content-Type": "application/x-www-form-urlencoded"
                                }
                            
                            params = {"message": ans}
                             
                            r = requests.post("https://notify-api.line.me/api/notify",
                                              headers=headers, params=params)
                            
                          #  print(r.status_code)
  except:

                        
                print('0')
                
                
  

      
    