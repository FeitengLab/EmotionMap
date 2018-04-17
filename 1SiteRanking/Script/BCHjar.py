# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 23:24:34 2018

@author: HCHO
"""
import os
import time
#BCH是用来求放入多个文件的最适宜lambda参数，lambdaTestResult为多个文件一起计算的结果。无需修改config.json的参数。
#将聚类好的文件放到Cluster文件夹下
#result即为最优凹壳结果
filenum=1
for i in range(1,filenum+1):  
    #读取Sample_Input_clustered.csv文件
    cluster=open('Cluster/Sample_Input_clustered{0}.csv'.format(i),'r')
    txt=cluster.read()
    cluster.close()
    
    #写入exampleData.csv文件
    exampleData=open('Input/exampleData.csv','w')
    exampleData.write(txt)
    exampleData.close()
    
    os.popen('java -jar BalancedConcave.jar')
    
    time.sleep(5)  #根据情况调整时间
    
    #会在Output文件夹下得到最优的exampleData.json和一份lambdaTestResult.csv
    while(True):
        if(os.path.exists('Output/exampleData.json')):
            os.rename('Output/exampleData.json','Output/result{0}.json'.format(i))  
            break
        else:
            time.sleep(10)
    
    lambdaTest=open('Output/lambdaTestResult.csv','r')
    Lambda=[]
    line=lambdaTest.readline()
    while(line):
        lam=line.split(',')[1]
        line=lambdaTest.readline()        
        Lambda.append(lam)
    balance=min(Lambda)
    minlambda=Lambda.index(balance)+1
    lambdaTest.close()
    
    fo=open('lamdbaResult.csv','a')
    fo.write(str(i)+','+str(minlambda)+','+balance)
    fo.close()