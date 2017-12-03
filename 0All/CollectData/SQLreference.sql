/*本文件包含了一些可能需要用到的SQL语句*/
/*创建Flickr照片表*/
CREATE TABLE flickr0
(id BIGINT PRIMARY KEY NOT NULL,
userid TEXT,
photo_date_taken DATE,
photo_date_uploaded BIGINT,
title TEXT,
description TEXT,
user_tags TEXT,
longitude FLOAT DEFAULT 0,
latitude FLOAT DEFAULT 0,
accuracy INTEGER DEFAULT 0,
download_url TEXT NOT NULL
);
CREATE INDEX iflickr_id0 ON flickr0(id);
CREATE INDEX iflickr_date0 ON flickr0(photo_date_taken);

/*添加情绪相关属性*/
ALTER TABLE flickr0 ADD facenum integer;
ALTER TABLE flickr0 ADD emotion json;

/*将数据文件导入表*/
COPY flickr0 FROM 'E:\BaiduNetdiskDownload\flickr_data\geotag_data'

/*从json数组中获取相应的属性*/
SELECT json_array_elements(emotion)->'ethnicity'->>'value' FROM flickr0 WHERE id=39961;

/*创建带有情绪值的Flickr人脸表*/
CREATE TABLE face
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
faceid serial PRIMARY KEY
);

CREATE INDEX iface_id ON face(id);
CREATE INDEX iface_userid ON face(userid);
CREATE INDEX iface_photo_date_taken ON face(photo_date_taken);
CREATE INDEX iface_facenum ON face(facenum);
CREATE INDEX iface_happiness ON face(happiness);
CREATE INDEX iface_neutral ON face(neutral);
CREATE INDEX iface_sadness ON face(sadness);
CREATE INDEX iface_disgust ON face(disgust);
CREATE INDEX iface_anger ON face(anger);
CREATE INDEX iface_fear ON face(fear);
CREATE INDEX iface_surprise ON face(surprise);
CREATE INDEX iface_smile_s ON face(smile_s);
CREATE INDEX iface_smile_v ON face(smile_v);
CREATE INDEX iface_gender ON face(gender);
CREATE INDEX iface_ethnicity ON face(ethnicity);
CREATE INDEX iface_age ON face(age);

