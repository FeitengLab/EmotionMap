# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:23:21 2017

@author: HCHO
"""
#修改fileName，path，API信息即可
#已将时间信息加入
import psycopg2
connection = psycopg2.connect(database="postgres", user="postgres", password="guyuan", host="localhost", port="5432")
cur = connection.cursor()

#创建列表
    
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
#插入数据
    

def InsertFaceTable(site,iline_list):
    sql_command_insertface = "INSERT INTO FaceTable_{0} VALUES({1})".format(site,iline_list)
    cur.execute(sql_command_insertface)
    connection.commit() 


   
def SelectData(dataName):
    try:
        sql_command_select="SELECT photoId,url FROM public.FaceTable_{0} WHERE faceNum is null limit 1;".format(dataName)
        cur.execute(sql_command_select)
        data=cur.fetchone()
        
        res = api.detect(image_url=data[1],return_attributes=["gender","age","smiling","emotion","facequality"])       
        i=len(res["faces"])
        #print i
        faceInfo=[]
        if i!=0:
    		 for k in range(0,i):
    			 faceInfo.append(res["faces"][k]["attributes"])
        faceIn = json.dumps(faceInfo)
        #print faceIn
        
        sql_command_update="UPDATE public.FaceTable_{0} SET faceNum={2},attributes='{3}' WHERE photoId={1}".format(dataName,data[0],i,faceIn)
        cur.execute(sql_command_update)
        
        connection.commit()
        return data[0]
    except Exception as e:
        print(e)
        connection.rollback()
        return None
    

from facepp import API
import json
#csv数据 photoId userid photoTakeTime photoUploadTime photoTitle photoDescription photoGeotag longitude latitude accuracy url
API_KEY = "oSzQJ7Owxqk2T5yZuIHKoJ3s_n11BDQP"
API_SECRET = "6wv-sD-NgKWm0kRK757UxUDsbuzj0TYs"

api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'
api = API(API_KEY, API_SECRET, srv=api_server_international)

fileName='10'
path="C:\\Users\\HCHO\\Desktop\\emotionData\\"+fileName+".csv"

#将csv文件路径储存倒flickrDataFile数组中             
CreateFaceTable(fileName)    
csv_read=open(path,'r')         
while True:

    line = csv_read.readline()
    if line:
		try:
			line_list = line.split() #按空格分割会将时间分为两个对象，因此变成12个
			face_url=line_list[11].replace("'","")
					
			strline=line_list[0]+','+line_list[1]+','+line_list[2]+" "+line_list[3]+','+line_list[4]+','+line_list[5]+','\
			+line_list[6]+','+line_list[7]+','+line_list[8]+','+line_list[9]+','+line_list[10]+','+line_list[11]    
			
			InsertFaceTable(fileName,strline)
		except:
			print 'error!'
    else:
        break
csv_read.close()
count=0
while True:
    photoID=SelectData(fileName)
    if photoID == None:
        break