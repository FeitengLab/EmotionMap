# coding:utf-8
# version:python3.5.1
# author:kyh

import flickrapi
import datetime
import psycopg2
import time


# flickr照片类
class flickr_photo(object):
    def __init__(self, photo_id, photo_site, photo_url):
        self.id = photo_id
        self.site = photo_site
        self.url = photo_url

    # 将照片插入数据库
    def insert_db(self, db_connection, db_cursor):
        try:
            sql_command_insert = "INSERT INTO photo(id,url,site) VALUES({0},'{1}','{2}')".format(self.id,
                                                                                                 self.url,
                                                                                                 self.site
                                                                                                 )
            db_cursor.execute(sql_command_insert)
            db_connection.commit()
            return True
        except Exception as e:
            with open('log.txt','a') as log:
                log.writelines(str(e))
            db_connection.rollback()
            return False


# 连接数据库
def db_connect():
    try:
        connection = psycopg2.connect(database="EmotionMap3", user="postgres",
                                      password="postgres", host="127.0.0.1", port="5432")
        cursor = connection.cursor()
        print("Database Connection has been opened completely!")
        return connection, cursor
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))


# 查询需要挖掘数据的地点
def query_site(db_connection, db_cursor):
    sql_command_select = "SELECT * FROM site WHERE start_query='FALSE' LIMIT 1"
    db_cursor.execute(sql_command_select)
    site = db_cursor.fetchone()
    # 如果存在这样的地点,记录经纬度进行挖掘
    if site is not None:
        site_name = site[1]
        lat = site[2]
        lon = site[3]
        sql_command_update = "UPDATE site SET start_query='TRUE' WHERE site_name='{0}'".format(site_name)
        db_cursor.execute(sql_command_update)
        db_connection.commit()
        return site_name, lat, lon
    # 不存在这样的地点,说明已经全部挖掘完毕
    else:
        return None, None, None


# flickr api信息
def flickrAPI():
    api_key = u'199ed59000c39dd0844b59d01fa7570c'
    api_secret = u'4a2ce28f1bb8a1fe'
    flickr = flickrapi.FlickrAPI(api_key, api_secret, cache=True)
    return flickr


# 计算时间
def compute_time(db_connection, db_cursor, site, latitude, longitude):
    DATE=datetime.date(2012,1,1)
    while(True):
        DATE2=DATE+datetime.timedelta(days=10)
        datemin ="{0}-{1}-{2}".format(DATE.year,DATE.month,DATE.day)
        datemax ="{0}-{1}-{2}".format(DATE2.year,DATE2.month,DATE2.day)
        DATE=DATE+datetime.timedelta(days=10)
        #print(datemin,datemax)
        get_photo_from_location(db_connection, db_cursor, site, latitude, longitude, datemin, datemax)
        if DATE.year==2017 and DATE.month==12:
            break

# 获取照片
def get_photo_from_location(db_connection, db_cursor, site, latitude, longitude, datemin, datemax):
    flickr = flickrAPI()
    # 获取所有图片
    try:
        time.sleep(3)
        photos = flickr.walk(lat=latitude, lon=longitude, radius=1,
                             min_taken_date=datemin, max_taken_date=datemax, per_page=500, extras='url_c')
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))
    # 获取每一张图片
    try:
        for photo_url in photos:
            url = photo_url.get('url_c')
            # 如果url不为空,将该图片插入数据库
            if url is not None:
                photo_id = int(photo_url.get('id'))
                photo = flickr_photo(photo_id, site, url)
                if photo.insert_db(db_connection, db_cursor):
                    print("Success! Photo id:" + str(photo_id) + "\tPhoto url:" + url)
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))


# 关闭数据库
def close_connection(connection):
    try:
        connection.close()
        print("Database Connection has been closed completely!")
        return True
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))


# 主操作步骤
if __name__ == '__main__':
    db_connection, db_cursor = db_connect()
    while(True):
        site, lat, lon= query_site(db_connection, db_cursor)
        if site is not None:
            compute_time(db_connection, db_cursor, site, lat, lon)
        else:
            print("All sites have been recorded!")
            break
    close_connection(db_connection)
