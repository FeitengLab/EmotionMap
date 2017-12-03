/*1创建带有情绪值的Flickr人脸表*/
CREATE TABLE face{0}
(id BIGINT NOT NULL,
userid TEXT,
photo_date_taken DATE,
photo_date_uploaded BIGINT,
title TEXT DEFAULT NULL,
description TEXT DEFAULT NULL,
user_tags TEXT DEFAULT NULL,
longitude FLOAT DEFAULT 0,
latitude FLOAT DEFAULT 0,
accuracy INTEGER DEFAULT 0,
download_url TEXT NOT NULL,
facenum INTEGER,
happiness FLOAT,
neutral FLOAT,
sadness FLOAT,
disgust FLOAT,
anger FLOAT,
fear FLOAT,
surprise FLOAT,
facequality_s FLOAT,
facequality_v FLOAT,
smile_s FLOAT,
smile_v FLOAT,
gender INTEGER,
ethnicity INTEGER,
age INTEGER,
point geometry(Point)
);

/*2将文件拷贝进去*/
COPY face{0}
FROM 'D:\\Users\\KYH\\Desktop\\EmotionMap\\FlickrEmotionData\\4face_all\\face{0}.csv' 
WITH csv;

/*将文件拷贝出来*/
COPY face{0}
TO 'D:\\Users\\KYH\\Desktop\\EmotionMap\\FlickrEmotionData\\4face_all\\face{0}.csv' 
WITH csv;

/*添加空间坐标信息*/
ALTER TABLE face{0} ADD point geometry(point,4326);

/*设置点等于坐标*/
UPDATE face{0} SET point = ST_SetSRID(ST_Point(longitude,latitude),4326);

/*3创建索引*/
CREATE INDEX iface_lon{0} ON face{0}(longitude);
CREATE INDEX iface_lat{0} ON face{0}(latitude);

CREATE INDEX iface_id{0} ON face{0}(id);
CREATE INDEX iface_userid{0} ON face{0}(userid);
CREATE INDEX iface_photo_date_taken{0} ON face{0}(photo_date_taken);
CREATE INDEX iface_facenum{0} ON face{0}(facenum);
CREATE INDEX iface_happiness{0} ON face{0}(happiness);
CREATE INDEX iface_neutral{0} ON face{0}(neutral);
CREATE INDEX iface_sadness{0} ON face{0}(sadness);
CREATE INDEX iface_disgust{0} ON face{0}(disgust);
CREATE INDEX iface_anger{0} ON face{0}(anger);
CREATE INDEX iface_fear{0} ON face{0}(fear);
CREATE INDEX iface_surprise{0} ON face{0}(surprise);
CREATE INDEX iface_smile_s{0} ON face{0}(smile_s);
CREATE INDEX iface_smile_v{0} ON face{0}(smile_v);
CREATE INDEX iface_gender{0} ON face{0}(gender);
CREATE INDEX iface_ethnicity{0} ON face{0}(ethnicity);
CREATE INDEX iface_age{0} ON face{0}(age);

CREATE INDEX iface_pt{0} ON face{0} USING gist(point);
CREATE INDEX iface_country{0} ON face{0}(country);

/*5添加国家信息*/
ALTER TABLE face{0} Add country text;

/*6将点和国家对应*/
UPDATE face0
SET country=t.admin
FROM countries AS t
WHERE ST_Intersects(face0.point,t.geom);

SELECT face0.point,countries.admin
FROM face0,countries
WHERE ST_Intersects(face0.point,countries.geom)
LIMIT 100;

/*4设置参考系*/
SELECT UpdateGeometrySRID('face0', 'point', 4326);

/*为国家创建空间索引*/
CREATE INDEX iadmin ON countries USING gist(ST_Transform(ST_SetSRID(geom,4326),4326));

/*
1.创建表
2.导入csv
3.创建索引
4.设置空间坐标系
5.添加国家字段
6.将点和国家对应
*/

SELECT
id,(
SELECT admin
FROM face0,countries
WHERE face0.country is null
ORDER BY face0.point <-> countries.geom 
LIMIT 1
) as closest
From face0
LIMIT 100;