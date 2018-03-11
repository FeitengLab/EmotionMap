﻿CREATE TABLE site
(id INTEGER PRIMARY KEY,
site_name CHARACTER VARYING(100) NOT NULL,
lat FLOAT NOT NULL,
lon FLOAT NOT NULL,
start_query BOOLEAN NOT NULL DEFAULT(FALSE)
);
CREATE INDEX site_name_index ON site(site_name);
CREATE INDEX start_query ON site(start_query);

CREATE TABLE photo
(id BIGINT PRIMARY KEY,
url TEXT NOT NULL,
owner CHARACTER VARYING (30),
owner_location CHARACTER VARYING (30),
site CHARACTER VARYING(100) NOT NULL,
lat FLOAT,
lon FLOAT,
photo_take_date DATE,
photo_upload BIGINT,
accuracy INTEGER,
geotag TEXT,
f_hasface BOOLEAN NOT NULL DEFAULT(FALSE),
start_detect BOOLEAN NOT NULL DEFAULT(FALSE),
start_info BOOLEAN NOT NULL DEFAULT(FALSE),
start_recog BOOLEAN NOT NULL DEFAULT(FALSE)
);
CREATE INDEX photo_id_index ON photo(id);
CREATE INDEX photo_lat_index ON photo(lat);
CREATE INDEX photo_lon_index ON photo(lon);
CREATE INDEX photo_date_index ON photo(photo_take_date);
CREATE INDEX photo_f_hasface_index ON photo(f_hasface);
CREATE INDEX photo_start_detect_index ON photo(start_detect);
CREATE INDEX photo_start_info_index ON photo(start_info);
CREATE INDEX photo_start_recog_index ON photo(start_recog);
CREATE INDEX photo_facenum_index ON photo(facenum);

ALTER TABLE photo ADD neighbourhood TEXT;
ALTER TABLE photo ADD locality TEXT;
ALTER TABLE photo ADD county TEXT;
ALTER TABLE photo ADD region TEXT;
ALTER TABLE photo ADD country TEXT;
ALTER TABLE photo DROP owner_location;

ALTER TABLE photo ADD emotion json;
ALTER TABLE photo ADD facenum INTEGER;
ALTER TABLE photo DROP f_hasface;

CREATE TABLE facepp
(id BIGINT PRIMARY KEY,
photo_id BIGINT NULL,
site CHARACTER VARYING(30) NOT NULL,
gender INTEGER NOT NULL,
age INTEGER NOT NULL,
smiling FLOAT NOT NULL,
smile_threshold FLOAT NOT NULL ,
glass TEXT NOT NULL
);
CREATE INDEX facepp_photo_id_index ON facepp(photo_id);

CREATE TABLE ms_emotion
(id SERIAL PRIMARY KEY,
photo_id BIGINT NOT NULL,
site CHARACTER(30) NOT NULL,
anger FLOAT NOT NULL,
contempt FLOAT NOT NULL,
disgust FLOAT NOT NULL,
fear FLOAT NOT NULL,
happiness FLOAT NOT NULL,
neutral FLOAT NOT NULL,
sadness FLOAT NOT NULL,
surprise FLOAT NOT NULL
);
CREATE INDEX ms_emotion_photo_id_index ON ms_emotion(photo_id);
CREATE INDEX ms_emotion_happiness ON ms_emotion(happiness);
CREATE INDEX ms_emotion_sadness ON ms_emotion(sadness);

SELECT photo.id,photo.coordinates,ms_emotion.happiness,ms_emotion.sadness
FROM ms_emotion JOIN photo ON photo_id=ms_emotion.photo_id LIMIT 3

ALTER TABLE ms_emotion ADD coordinates POINT;
ALTER TABLE ms_emotion ADD photo_take_date DATE;
ALTER TABLE ms_emotion ADD start_join BOOLEAN NOT NULL DEFAULT(FALSE);


create table face(
id serial primary key,
photo_id bigint,
coordinates point,
photo_time date,
happy float,
sad float);

create index index_id on face(id);
create index index_co on face using gist(coordinates);
create index index_ti on face(photo_time);
create index index_ha on face(happy);
create index index_sa on face(sad);

SELECT st_distance(st_geomfromtext('point({0} {1})',4326),st_geomfromtext('point(-74.0095 40.7064)',4326),true)
