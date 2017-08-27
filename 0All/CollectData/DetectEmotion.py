# coding:utf-8
# version:python3.5.1
# author:kyh
# detect emotion information of each photo

import json

import psycopg2
import requests

API_KEY = "oSzQJ7Owxqk2T5yZuIHKoJ3s_n11BDQP"
API_SECRET = "6wv-sD-NgKWm0kRK757UxUDsbuzj0TYs"
TABLE_ID = 0


class CloudDatabase(object):
    # Init database and input ip
    # 初始化数据库并传入ip
    def __init__(self, database, user, password, ip="127.0.0.1", port="5432"):
        self.database = database
        self.user = user
        self.password = password
        self.ip = ip
        self.port = port

    # Connect database and set input as host, return connection and cursor
    # 连接ip端数据库并返回connection和cursor
    def db_connect(self):
        self.connection = psycopg2.connect(database=self.database, user=self.user,
                                           password=self.password, host=self.ip, port=self.port)
        self.cursor = self.connection.cursor()

    # Write log file
    # 输出日志
    def write_log(self, e):
        self.connection.rollback()
        with open("log.txt", 'a') as log_file:
            log_file.writelines(str(e))

    # 查询没有探测人脸的照片并获取id和url
    def query_photo(self):
        sql_command = "SELECT id, download_url FROM flickr{0} WHERE facenum IS NULL LIMIT 1;".format(TABLE_ID)
        self.cursor.execute(sql_command)
        result = self.cursor.fetchone()
        if result == None:
            return None, None
        else:
            return result[0], result[1]

    # 向人脸照片添加情绪属性
    # 不存在人脸
    def change_nofaces(self, img_id):
        try:
            sql_command = "UPDATE flickr{0} SET facenum=0 WHERE id={1}".format(TABLE_ID, img_id)
            self.cursor.execute(sql_command)
            self.connection.commit()
        except Exception as e:
            self.write_log(e)

    # 存在人脸
    def change_faces(self, img_id, count, emotion):
        try:
            face_info = []
            for k in range(0, count):
                face_info.append(emotion["faces"][k]["attributes"])
            face_info = json.dumps(face_info)
            sql_command = "UPDATE flickr{0} SET facenum={1},emotion='{2}' WHERE id={3}".format(TABLE_ID, count,
                                                                                               face_info,
                                                                                               img_id)
            self.cursor.execute(sql_command)
            self.connection.commit()
        except Exception as e:
            self.write_log(e)


# 探测人的情绪
def detect_emotion(img_url):
    url = "https://api-us.faceplusplus.com/facepp/v3/detect"
    params = {
        "api_key": API_KEY,
        "api_secret": API_SECRET,
        "image_url": img_url,
        "return_attributes": "gender,age,smiling,emotion,facequality,ethnicity"
    }
    r = requests.post(url, params)
    face_info = json.loads(r.content.decode())
    return len(face_info["faces"]), face_info


if __name__ == '__main__':
    try:
        # 连接数据库
        # database = CloudDatabase("Flickr1", "postgres", "postgres", "47.89.209.207")
        database = CloudDatabase("Flickr1", "postgres", "postgres", "127.0.0.1")
        database.db_connect()
        # 查询未被搜索的人脸
        img_id, url = database.query_photo()
        # 说明没有结束
        while id != None:
            # 获取人脸的数目和情绪信息
            face_count, face_info = detect_emotion(url)
            # 如果无人脸
            if face_count == 0:
                database.change_nofaces(img_id)
            # 如果有人脸
            else:
                database.change_faces(img_id, face_count, face_info)
            # 继续查询未被搜索的人脸
            img_id, url = database.query_photo()
    except Exception as e:
        with open("log.txt", 'a') as log_file:
            log_file.writelines(str(e))
