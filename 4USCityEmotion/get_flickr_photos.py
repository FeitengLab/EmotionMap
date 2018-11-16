# coding:utf-8
# version:python3.5.1
# author:kyh

import flickrapi
import datetime
import psycopg2
import time


# flickr照片类
class flickr_photo(object):
    def __init__(self, photo_id, photo_city, photo_url):
        self.id = photo_id
        self.city = photo_city
        self.url = photo_url

    # 将照片插入数据库
    def insert_db(self, db_connection, db_cursor):
        try:
            sql_command_insert = "INSERT INTO photo(id,url,city) VALUES({0},'{1}','{2}')".format(self.id,
                                                                                                 self.url,
                                                                                                 self.city
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
        connection = psycopg2.connect(database="PlaceEmotion", user="postgres",
                                      password="postgres", host="127.0.0.1", port="5432")
        cursor = connection.cursor()
        print("Database Connection has been opened completely!")
        return connection, cursor
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))


# 查询需要挖掘数据的地点
def query_location(db_connection, db_cursor):
    sql_command_select = "SELECT id, city_name, lat, lon FROM location WHERE start_query='FALSE' LIMIT 1"
    db_cursor.execute(sql_command_select)
    db_connection.commit()
    location = db_cursor.fetchone()
    # 如果存在这样的地点,记录经纬度进行挖掘
    if location is not None:
        location_id = location[0]
        city = location[1]
        lat = location[2]
        lon = location[3]
        sql_command_update = "UPDATE location SET start_query='TRUE' WHERE id ='{0}'".format(location_id)
        db_cursor.execute(sql_command_update)
        db_connection.commit()
        return city, lat, lon
    # 不存在这样的地点,说明已经全部挖掘完毕
    else:
        return None, None, None


# flickr api信息
def query_api(db_connection, db_cursor):
    sql_command_select = "SELECT key, secret FROM API WHERE type = 'flickr' AND start_use = FALSE LIMIT 1"
    db_cursor.execute(sql_command_select)
    db_connection.commit()
    api = db_cursor.fetchone()
    # 如果存在这样的API,记录API进行挖掘
    if api is not None:
        key = api[0]
        secret = api[1]
        sql_command_update = "UPDATE API SET start_use='TRUE' WHERE key='{0}'".format(key)
        db_cursor.execute(sql_command_update)
        db_connection.commit()

        api_key = u'{0}'.format(key)
        api_secret = u'{0}'.format(secret)
        flickr = flickrapi.FlickrAPI(api_key, api_secret, cache=True)
        print("API:", api_key, api_secret)
        return flickr, key
    # 不存在这样的API,说明已经全部挖掘完毕
    else:
        return None, None


# 计算时间
def compute_time(db_connection, db_cursor, location, latitude, longitude, flickr_api):
    DATE=datetime.date(2012,1,1)
    while(True):
        DATE2=DATE+datetime.timedelta(days=10)
        datemin ="{0}-{1}-{2}".format(DATE.year,DATE.month,DATE.day)
        datemax ="{0}-{1}-{2}".format(DATE2.year,DATE2.month,DATE2.day)
        DATE=DATE+datetime.timedelta(days=10)
        #print(datemin,datemax)
        get_photo_from_location(db_connection, db_cursor, location, latitude, longitude, datemin, datemax, flickr_api)
        if DATE.year==2018 and DATE.month==11:
            break

# 获取照片
def get_photo_from_location(db_connection, db_cursor, location, latitude, longitude, datemin, datemax, flickr):
    # 获取所有图片
    try:
        time.sleep(2)
        #latitude = 48.8584
        #longitude = 2.2945
        photos = flickr.walk(lat=latitude, lon=longitude, radius=1,
                             min_taken_date=datemin, max_taken_date=datemax, per_page=500, extras='url_c')
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))
    # 获取每一张图片
    try:
        for photo_url in photos:
            url = photo_url.get('url_c')
            print(url)
            # 如果url不为空,将该图片插入数据库
            if url is not None:
                photo_id = int(photo_url.get('id'))
                photo = flickr_photo(photo_id, location, url)
                if photo.insert_db(db_connection, db_cursor):
                    print("Success! Photo id:" + str(photo_id) + "\tPhoto url:" + url)
    except Exception as e:
        with open('log.txt','a') as log:
            log.writelines(str(e))


def release_api(db_connection, db_cursor, api_key):
    try:
        sql_command_update = "UPDATE API SET start_use = FALSE WHERE key = '{0}'".format(api_key)
        db_cursor.execute(sql_command_update)
        db_connection.commit()
    except Exception as e:
        db_connection.rollback()

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
    flickr, api_key = query_api(db_connection, db_cursor)
    location, lat, lon= query_location(db_connection, db_cursor)
    while location is not None:
        compute_time(db_connection, db_cursor, location, lat, lon, flickr)
        location, lat, lon= query_location(db_connection, db_cursor)
    print("All locations have been recorded!")
    release_api(db_connection, db_cursor, api_key)
    close_connection(db_connection)
