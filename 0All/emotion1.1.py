
import psycopg2
connection = psycopg2.connect(database="postgres", user="postgres", password="guyuan", host="localhost", port="5432")
cur = connection.cursor()

#创建列表
    
def CreateFaceTable(pointDataName):
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
CREATE INDEX if not exists iflickr__geoDate{0} ON public.FaceTable_{0}(photoTakeDate);'''.format(pointDataName))
    connection.commit()
#插入数据
    

def InsertFaceTable(site,iline_list):
    sql_command_insertface = "INSERT INTO FaceTable_{0} VALUES({1})".format(site,iline_list)
    cur.execute(sql_command_insertface)
    connection.commit() 
   
#import csv
from facepp import API
import os
import json
#csv数据name photoId userid photoTakeTime photoUploadTime photoTitle photoDescription photoGeotag longitude latitude accuracy url
API_KEY = "oSzQJ7Owxqk2T5yZuIHKoJ3s_n11BDQP"
API_SECRET = "6wv-sD-NgKWm0kRK757UxUDsbuzj0TYs"
api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'
api = API(API_KEY, API_SECRET, srv=api_server_international)

path="C:\\Users\\HCHO\\Desktop\\emotionData"
flickrDataFileUrl=[]
flickrDataName=[]
#将os.walk在元素中提取的值，分别放到root（根目录），dirs（目录名），files（文件名）中。
#将csv文件路径储存倒flickrDataFile数组中 
for root,dirs,files in os.walk(path):  
    for file in files:
        if ".csv" in file:
            flickrDataFileUrl.append(os.path.join(root,file))
            flickrDataName.append(file.replace('.csv',''))
            
for j in range(0,3):
    CreateFaceTable(flickrDataName[j])    
    datafile=flickrDataFileUrl[j]
    csv_read=open(datafile,'r')
                
    for line in csv_read: 
        try:
            line_list = line.split('\t')
            face_url=line_list[10].replace("'","")
    
            res = api.detect(image_url=face_url,return_attributes=["gender","age","smiling","emotion","facequality"])       
            i=len(res["faces"])
            #print i
            faceInfo=[]
            if i!=0:
                for k in range(0,i):
                    faceInfo.append(res["faces"][k]["attributes"])
            faceIn = json.dumps(faceInfo)
            #print faceIn
                
            strline=line_list[0]+','+line_list[1]+','+line_list[2]+','+line_list[3]+','+line_list[4]+','+line_list[5]+','\
            +line_list[6]+','+line_list[7]+','+line_list[8]+','+line_list[9]+','\
            +line_list[10]+','+str(i)+','+"'"+faceIn+"'"
                
        
            InsertFaceTable(flickrDataName[j],strline)     
        except:
            print 'error!'             
    csv_read.close()