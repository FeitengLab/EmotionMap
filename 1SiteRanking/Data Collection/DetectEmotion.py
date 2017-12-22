# coding:utf-8
# version:python3.5.1
# author:kyh
# detect emotion information of each photo

import json

import psycopg2
import requests

API_KEY = "oSzQJ7Owxqk2T5yZuIHKoJ3s_n11BDQP"
API_SECRET = "6wv-sD-NgKWm0kRK757UxUDsbuzj0TYs"


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
            log_file.writelines("[Errno {0}] \n".format(e))

    # 查询没有探测人脸的照片并获取id和url
    def query_photo(self):
        sql_command = "SELECT id, url FROM photo WHERE start_detect = false LIMIT 1;"
        self.cursor.execute(sql_command)
        result = self.cursor.fetchone()
        if result == None:
            return None, None
        else:
            id = result[0]
            url = result[1]
            sql_command = "UPDATE photo SET start_detect=true WHERE id={0}".format(id)
            self.cursor.execute(sql_command)
            self.connection.commit()
            return id, url

    # 向人脸照片添加情绪属性
    # 不存在人脸
    def change_nofaces(self, img_id):
        try:
            sql_command = "UPDATE photo SET facenum=0 WHERE id={0}".format(img_id)
            self.cursor.execute(sql_command)
            self.connection.commit()
        except Exception as e:
            self.write_log(e)

    # 存在人脸
    def change_faces(self, img_id, count, emotion):
        try:
            face_info = []
            for k in range(0, count):
                # 如果人脸的数目大于5
                try:
                    face_info.append(emotion["faces"][k]["attributes"])
                except Exception as e:
                    self.write_log(e)
            face_info = json.dumps(face_info)
            sql_command = "UPDATE photo SET facenum={0},emotion='{1}' WHERE id={2}".format(count, face_info,
                                                                                           img_id)
            self.cursor.execute(sql_command)
            self.connection.commit()
        except Exception as e:
            self.write_log(e)


# 探测人的情绪
def detect_emotion(img_url):
    try:
        url = "https://api-us.faceplusplus.com/facepp/v3/detect"
        params = {
            "api_key": API_KEY,
            "api_secret": API_SECRET,
            "image_url": img_url,
            "return_attributes": "gender,age,smiling,emotion,facequality,ethnicity"
        }
        r = requests.post(url, params)
        # 如果没有超过并发限制
        if r.status_code != 403:
            face_info = json.loads(r.content.decode())
            try:
                if len(face_info["faces"]) > -1:
                    return len(face_info["faces"]), face_info
                else:
                    return None, None
            except Exception as e:
                with open("log.txt", 'a') as log_file:
                    log_file.writelines("[Errno {0}] \n".format(e))
                return None, None
        else:
            return "403", None
    except Exception as  e:
        with open("log.txt", 'a') as log_file:
            log_file.writelines("[Errno {0}] \n".format(e))


if __name__ == '__main__':
    # 连接数据库
    # database = CloudDatabase("Flickr1", "postgres", "postgres", "47.89.209.207")
    database = CloudDatabase("EmotionMap", "postgres", "postgres", "127.0.0.1")
    database.db_connect()
    # 查询未被搜索的人脸
    img_id, url = database.query_photo()
    # 说明没有结束
    while img_id != None:
        try:
            # 获取人脸的数目和情绪信息
            face_count, face_info = detect_emotion(url)
            # 如果并发超过限值则重复
            if face_count == "403":
                continue
            # 如果图片解析错误则跳过进入下一条
            elif face_count == None:
                database.change_nofaces(img_id)
                img_id, url = database.query_photo()
                continue
            # 如果无人脸则facenum设为0
            if face_count == 0:
                database.change_nofaces(img_id)
            # 如果有人脸则记录人脸数目和具体情绪信息
            else:
                database.change_faces(img_id, face_count, face_info)
            # 继续查询未被搜索的人脸
            img_id, url = database.query_photo()
        except Exception as e:
            with open("log.txt", 'a') as log_file:
                log_file.writelines("[Errno {0}] \n".format(e))
