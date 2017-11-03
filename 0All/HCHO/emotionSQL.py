# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:53:38 2017

@author: HCHO
"""
# 数据库信息
import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="guyuan", host="localhost", port="5432")
cur = connection.cursor()


# 创建列表
def CreateDetectTable(pointDataName):
    cur.execute('''create table if not exists public.detectEmotionInfo_{0}(
ID bigserial primary key not null ,
image_id bigint,
faceNum real,
gender varchar(8),
age smallint,
smile real,
anger real,
disgust real,
fear real,
happiness real,
neutral real,
sadness real,
suprise real,
facequality real);
CREATE INDEX if not exists Detect_geoId{0} ON public.detectEmotionInfo_{0}(image_id);'''.format(pointDataName))
    connection.commit()


def CreateFaceTable(pointDataName):
    cur.execute('''create table if not exists public.FaceTable_{0}(
photoId bigint primary key not null,
userid TEXT,
photoTakeDate DATE,
photoUploadTime bigint,
photoTitle TEXT,
photoDescription TEXT,
photoGeotag TEXT,
longitude real,
latitude real,
accuracy smallint,
url  TEXT not null);
CREATE INDEX if not exists iflickr_geoId{0} ON public.FaceTable_{0}(photoId);
CREATE INDEX if not exists iflickr__geoDate{0} ON public.FaceTable_{0}(photoTakeDate);'''.format(pointDataName))
    connection.commit()


# 插入数据
def InsertDetectTable(pointDataName, image_id, iNum, iGender, iAge, iSmile, iAnger, iDisgust, iFear, iHappiness,
                      iNeutral, iSadness, iSurprise, iFacequality):
    sql_command_insert = "INSERT INTO detectEmotionInfo_{0}\
    (image_id,faceNum,gender,age,smile,anger,disgust,fear,happiness,neutral,sadness,suprise,facequality)\
    VALUES ({1},{2},'{3}',{4},{5},{6},{7},{8},{9},{10},{11},{12},{13})" \
        .format(pointDataName, image_id, iNum, iGender, iAge, iSmile, iAnger, iDisgust, iFear, iHappiness, iNeutral,
                iSadness, iSurprise, iFacequality)
    cur.execute(sql_command_insert)
    connection.commit()


def InsertFaceTable(site, iline_list):
    sql_command_insertface = "INSERT INTO FaceTable_{0} VALUES({1})".format(site, iline_list)
    cur.execute(sql_command_insertface)
    connection.commit()


# import csv
from facepp import API
import os

# csv数据name photoId userid photoTakeTime photoUploadTime photoTitle photoDescription photoGeotag longitude latitude accuracy url
API_KEY = "oSzQJ7Owxqk2T5yZuIHKoJ3s_n11BDQP"
API_SECRET = "6wv-sD-NgKWm0kRK757UxUDsbuzj0TYs"
api_server_international = 'https://api-us.faceplusplus.com/facepp/v3/'
api = API(API_KEY, API_SECRET, srv=api_server_international)

path = "C:\\Users\\HCHO\\Desktop\\data"
flickrDataFileUrl = []
flickrDataName = []
# 将os.walk在元素中提取的值，分别放到root（根目录），dirs（目录名），files（文件名）中。
# 将csv文件路径储存倒flickrDataFile数组中
for root, dirs, files in os.walk(path):
    for file in files:
        if ".csv" in file:
            flickrDataFileUrl.append(os.path.join(root, file))
            flickrDataName.append(file.replace('.csv', ''))
for j in range(0, 2):
    CreateDetectTable(flickrDataName[j])
    CreateFaceTable(flickrDataName[j])

    datafile = flickrDataFileUrl[j]
    # csv_read= csv.reader(open(datafile,'r'))  #按逗号分割，返回对象为list，不适用于本数据
    csv_read = open(datafile, 'r')
    # faceAttributesWriter=csv.writer(open("C:/Users/HCHO/Desktop/AttributeData.csv","ab"))
    fileWriter = open(path + "\\" + flickrDataName[j] + ".csv", "a")

    for line in csv_read:
        line_list = line.split()  # 按空格分割会将时间分为两个对象，因此变成13个
        face_url = line_list[12].replace("'", "")

        strline = line_list[1] + ',' + line_list[2] + ',' + line_list[3] + ' ' + line_list[4] + ',' \
                  + line_list[5] + ',' + line_list[6] + ',' + line_list[7] + ',' + line_list[8] + ',' + line_list[
                      9] + ',' \
                  + line_list[10] + ',' + line_list[11] + ',' + line_list[12]

        # print face_one
        InsertFaceTable(flickrDataName[j], strline)
        '''
        InsertFaceTable(line_list[0],long(line_list[1]),line_list[2],line_list[3],line_list[4],\
                        long(line_list[5]),line_list[6],line_list[7],line_list[8],float(line_list[9]),\
                        float(line_list[10]),int(line_list[11]),line_list[12])
        '''
        res = api.detect(image_url=face_url, return_attributes=["gender", "age", "smiling", "emotion", "facequality"])
        # print res["faces"][0]["attributes"]
        i = len(res["faces"])
        if i != 0:
            fileWriter.write(line)
        for i in range(0, i):
            image_id = long(line_list[1])
            num = i + 1
            gender = res["faces"][i]["attributes"]["gender"]["value"]
            age = res["faces"][i]["attributes"]["age"]["value"]
            smile = res["faces"][i]["attributes"]["smile"]["value"]
            anger = res["faces"][i]["attributes"]["emotion"]["anger"]
            disgust = res["faces"][i]["attributes"]["emotion"]["disgust"]
            fear = res["faces"][i]["attributes"]["emotion"]["fear"]
            happiness = res["faces"][i]["attributes"]["emotion"]["happiness"]
            neutral = res["faces"][i]["attributes"]["emotion"]["neutral"]
            sadness = res["faces"][i]["attributes"]["emotion"]["sadness"]
            surprise = res["faces"][i]["attributes"]["emotion"]["surprise"]
            facequality = res["faces"][i]["attributes"]["facequality"]["value"]

            InsertDetectTable(line_list[0], image_id, num, gender, age, smile, anger, \
                              disgust, fear, happiness, neutral, sadness, surprise, facequality)
            '''
            faceAttributesWriter.writerow([image_id,num,gender,age,smile,anger,\
                   disgust,fear,happiness,neutral,sadness,surprise,facequality])
            '''
