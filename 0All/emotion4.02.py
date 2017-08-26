# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:49:12 2017

@author: HCHO
"""
#功能：随机检测一个表中照片的facenum及attribus
#修改 数据库信息，API信息，文件名即可

import json
from facepp import API
import psycopg2
#数据库信息
connection = psycopg2.connect(database="postgres", user="postgres", password="guyuan", host="localhost", port="5432")
cur = connection.cursor()

#API信息
API_KEY = "oSzQJ7Owxqk2T5yZuIHKoJ3s_n11BDQP"
API_SECRET = "6wv-sD-NgKWm0kRK757UxUDsbuzj0TYs"

#文件名(表名中facetable_后部分)
flickrDataName='10'

#随机选取faceNum为null的项进行detect，获取facenum及attributes(json格式)并更新。返回值确认是否当结束
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

#主流程
if __name__ == '__main__':      
    api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'
    api = API(API_KEY, API_SECRET, srv=api_server_international)
    
    while True:
            photoID=SelectData(flickrDataName)
            if photoID == None:
                break