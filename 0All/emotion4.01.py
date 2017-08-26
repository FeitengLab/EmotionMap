# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:33:58 2017

@author: HCHO
"""
#功能：逐一读取数据并存入数据库
#修改  数据库信息，path即可


import os
import psycopg2
#数据库信息
connection = psycopg2.connect(database="postgres", user="postgres", password="guyuan", host="localhost", port="5432")
cur = connection.cursor()

#文件所在文件夹path
path="D:\\emotionData"


#csv数据 photoId userid photoTakeTime photoUploadTime photoTitle photoDescription photoGeotag longitude latitude accuracy url
#创建列表(包含照片的十一个基本信息及faceNum和attributes)及photoId、photoTakeDate的索引
def CreateFaceTable(dataName):
    cur.execute('''create table if not exists public.FaceTable_{0}(
photoId bigint primary key not null,
userid TEXT,
photoTakeDate timestamp,
photoUploadTime bigint,
photoTitle TEXT,
photoDescription TEXT,
photoGeotag TEXT,
longitude real,
latitude real,
accuracy smallint,
url  TEXT not null,
faceNum smallint,
attributes json);
CREATE INDEX if not exists iflickr_geoId{0} ON public.FaceTable_{0}(photoId);
CREATE INDEX if not exists iflickr__geoDate{0} ON public.FaceTable_{0}(photoTakeDate);'''.format(dataName))
    connection.commit()

#复制数据
def CopyFaceTable(site,csvpath):
    sql_command_insertface = "COPY FaceTable_{0} from '{1}' with csv header".format(site,csvpath)
    cur.execute(sql_command_insertface)
    connection.commit() 
    
#插入数据   
def InsertFaceTable(site,iline_list):
    sql_command_insertface = "INSERT INTO FaceTable_{0} VALUES({1})".format(site,iline_list)
    cur.execute(sql_command_insertface)
    connection.commit() 

#主流程
if __name__ == '__main__':    
    #两个列表储存文件路径和文件名
    flickrDataFilePath=[]
    flickrDataName=[]
    
    #搜索path文件夹下的csv文件，提取其路径、文件名，储存到列表中
    for root,dirs,files in os.walk(path):  
        for file in files:
            if ".csv" in file:
                flickrDataFilePath.append(os.path.join(root,file))
                flickrDataName.append(file.replace('.csv',''))
    
    #逐一遍历文件，创建表、按行读取并处理后插入表中          
    for i in range(0,3):            
        CreateFaceTable(flickrDataName[i])    
        
        csv_read=open(flickrDataFilePath[i],'r')         
        while True:    
            line = csv_read.readline()
            if line:
                try:   
                    #按\t分割；向‘项’中添加逗号，以便直接插入表中
                    line_list = line.split('\t') 
                    face_url=line_list[10].replace("'","")               
                    strline=line_list[0]+','+line_list[1]+','+line_list[2]+','+line_list[3]+','+line_list[4]+','\
                    +line_list[5]+','+line_list[6]+','+line_list[7]+','+line_list[8]+','+line_list[9]+','+line_list[10]  
        			
                    InsertFaceTable(flickrDataName[i],strline)
                except:               
        			   print 'error!'
            else:
                break
        csv_read.close()
        
    '''        
        try:		
            CopyFaceTable(flickrDataName[i],flickrDataFilePath[i])           
        except:               
            	print 'error!'
    '''           