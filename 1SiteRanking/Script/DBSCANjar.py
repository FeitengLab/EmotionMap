# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 18:38:12 2018

@author: HCHO
"""
import os
import time

#输入参数
filenum=2
eps=0.001
minPts=0.005
lamda=50
#将各景点坐标按格式存在Input文件夹下，命名为Sample1..Sample2..Sample3..这样
#将config.json改名为config0.json

for i in range(1,filenum+1):  
    #改写config.json
    con0=open('config0.json','r') 
    config=con0.read()
    con0.close()
    config=config.replace("0.01",str(eps),1)  #eps:28800
    config=config.replace('0.05',str(minPts),1)   #minPts: 0.05
    config=config.replace('50',str(lamda),1)     #lambda: 50
    
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
       
    #文件重命名
    while(True):
        if(os.path.exists('Temp/Sample_Input_clustered.csv') and os.path.exists('result.json') ):  
            os.rename('Temp/Sample_Input_clustered.csv','Sample_Input_clustered{0}.csv'.format(i))
            os.rename('result.json','result{0}.json'.format(i))
            break
        else:
            time.sleep(10)