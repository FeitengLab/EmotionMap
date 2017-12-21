# coding:utf-8
# version:python3.5.1
# author:kyh

import flickrapi
import psycopg2
import json
import time


# 图片经纬度信息类
class photo_coordinates():
    def __init__(self, photo_id, photo_owner, photo_post_date, photo_take_date, photo_lat, photo_lon, photo_accuracy,
                 neighbourhood, locality, county, region, country, geotag):
        self.photo_id = photo_id
        self.photo_owner = photo_owner
        self.photo_upload = photo_post_date
        self.photo_take_date = photo_take_date
        self.photo_lat = photo_lat
        self.photo_lon = photo_lon
        self.photo_accuracy = photo_accuracy
        self.neighbourhood = neighbourhood
        self.locality = locality
        self.county = county
        self.country = country
        self.region = region
        self.geotag = geotag

    # 输入经纬度等信息
    def input_coordinates(self, connection, cursor):
        try:
            sql_command_update = "UPDATE photo SET owner='{0}',photo_upload={1},photo_take_date='{2}'," \
                                 "lat={3},lon={4},accuracy={5},neighbourhood='{6}'," \
                                 "locality='{7}',county='{8}',country='{9}',region='{10}'," \
                                 "geotag='{11}' WHERE id={12}".format(
                self.photo_owner, self.photo_upload, self.photo_take_date, self.photo_lat, self.photo_lon,
                self.photo_accuracy, self.neighbourhood, self.locality, self.county,
                self.country, self.region, self.geotag, self.photo_id)
            cursor.execute(sql_command_update)
            connection.commit()
            print("Success Input Coordinates!")
            return True
        except Exception as e:
            with open('log.txt', 'a') as log_file:
                log_file.writelines(str(e))
            connection.rollback()
            return False


# 连接数据库
def db_connect():
    connection = psycopg2.connect(database="EmotionMap", user="postgres",
                                  password="postgres", host="127.0.0.1", port="5432")
    cursor = connection.cursor()
    print("Database Connection has been opened completely!")
    return connection, cursor


# 查询需要补充信息的照片
def query_photo(db_connection, db_cursor):
    sql_command_select = "SELECT id FROM photo WHERE start_info='FALSE' LIMIT 1"
    db_cursor.execute(sql_command_select)
    photo = db_cursor.fetchone()
    if photo is not None:
        photo_id = photo[0]
        try:
            sql_command_update = "UPDATE photo SET start_info='TRUE' WHERE id={0}".format(photo_id)
            db_cursor.execute(sql_command_update)
            db_connection.commit()
            return photo_id
        except Exception as e:
            with open('log.txt', 'a') as log_file:
                log_file.writelines(str(e))
            db_connection.rollback()
            return None
    else:
        return None


# flickr api信息
def flickrAPI():
    api_key = u'199ed59000c39dd0844b59d01fa7570c'
    api_secret = u'4a2ce28f1bb8a1fe'
    flickr = flickrapi.FlickrAPI(api_key, api_secret, cache=True)
    return flickr


# 获取图片的经纬度坐标等信息
def get_photo_coordinates(connection, cursor, photo_id):
    flickr = flickrAPI()
    photo_info = flickr.photos.getInfo(photo_id=photo_id, format='json')
    photo_info = photo_info.decode()
    photo_info = json.loads(photo_info)
    # 解析结果
    try:
        photo_owner = photo_info["photo"]["owner"]["nsid"]
    except:
        photo_owner = ""
    try:
        photo_post_date = photo_info["photo"]["dates"]["posted"]
    except:
        photo_post_date = ""
    try:
        photo_take_date = photo_info["photo"]["dates"]["taken"]
    except:
        photo_take_date = ""
    try:
        photo_lat = photo_info["photo"]["location"]["latitude"]
    except:
        photo_lat = ""
    try:
        photo_lon = photo_info["photo"]["location"]["longitude"]
    except:
        photo_lon = ""
    try:
        photo_accuracy = photo_info["photo"]["location"]["accuracy"]
    except:
        photo_accuracy = ""
    try:
        neighbourhood = photo_info["photo"]["location"]["neighbourhood"]["_content"]
    except:
        neighbourhood = ""
    try:
        locality = photo_info["photo"]["location"]["locality"]["_content"]
    except:
        locality = ""
    try:
        county = photo_info["photo"]["location"]["county"]["_content"]
    except:
        county = ""
    try:
        region = photo_info["photo"]["location"]["region"]["_content"]
    except:
        region = ""
    try:
        country = photo_info["photo"]["location"]["country"]["_content"]
    except:
        country = ""
    try:
        geotag = ""
        for tag in photo_info["photo"]["tags"]["tag"]:
            tag_raw = tag['raw']
            geotag = "{0}{1};".format(str(geotag), str(tag_raw))
    except:
        geotag = ""
    # 将信息录入数据库
    coordinates = photo_coordinates(photo_id, photo_owner, photo_post_date, photo_take_date, photo_lat, photo_lon,
                                    photo_accuracy, neighbourhood, locality, county, region, country, geotag)
    return coordinates.input_coordinates(connection, cursor)


# 关闭数据库
def close_connection(connection):
    try:
        connection.close()
        print("Database Connection has been closed completely!")
        return True
    except Exception as e:
        with open('log.txt', 'a') as log_file:
            log_file.writelines(str(e))


# 主要步骤
if __name__ == '__main__':
    connection, cursor = db_connect()
    photo = query_photo(connection, cursor)
    while photo is not None:
        try:
            get_photo_coordinates(connection, cursor, photo)
            time.sleep(1)
            photo = query_photo(connection, cursor)
        except Exception as  e:
            with open('log.txt', 'a') as log_file:
                log_file.writelines(str(e))
    close_connection(connection)
    print("All photos have information!")
