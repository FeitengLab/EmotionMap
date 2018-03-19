# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:38:12 2018

@author: HCHO
"""
import os
import time

#输入参数
filenum=1
eps=28800
minPts=0.05
lamda=50
#将各景点坐标按格式存在Input文件夹下，命名为Sample1..Sample2..Sample3..这样
#将config.json改名为config0.json

for i in range(1,filenum+1):  #1...98
    #改写config.json
    con0=open('config0.json','r') 
    config=con0.read()
    con0.close()
    config.replace('28800',eps,1)  #eps:28800
    config.replace('0.05',minPts,1)   #minPts: 0.05
    config.replace('50',lamda,1)     #lambda: 50
    
    con=open('config.json','w') 
    con.write(config)
    con.close()
    
    #改写Sample_Input.csv
    Simple=open('Input/Sample{0}.csv'.format(i),'r')
    Simple_in=Simple.read()
    Simple.close()
    
    Simple_input=open('Input/Sample_Input.csv','w')
    Simple_input.write(Simple_in)
    Simple_input.close()
    
    #执行命令行
    os.popen('java -jar DBSCAN4LBSN.jar')
        
    time.sleep(2)
    #将结果读出并重新存储到reselt1.json
    result=open('result.json','r')
    finallyResult=result.read()
    result.close()
    
    resultjson=open('result{0}.json'.format(i),'w')
    resultjson.write(finallyResult)
    resultjson.close()