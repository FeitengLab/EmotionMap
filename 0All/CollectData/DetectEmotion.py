# coding:utf-8
# version:python3.5.1
# author:kyh
# detect emotion information of each photo

import requests
import psycopg2
import json

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
        with open("log.txt", 'a') as log_file:
            log_file.writelines(str(e))


    def query_photo(self):
        sql_command="SELECT id, download_url FROM {0} WHERE facenum IS NULL LIMIT 1;"


def detect_emotion(img_url):
    url = "https://api-us.faceplusplus.com/facepp/v3/detect"
    params = {
        "api_key": API_KEY,
        "api_secret": API_SECRET,
        "image_url": img_url,
        "return_attributes": "gender,age,smiling,emotion,facequality,ethnicity"
    }
    r = requests.post(url, params)
    print(r.content)
    face_info=json.loads(r.content.decode())
    if len(face_info["faces"]) >0:
        print(True)
    for face in face_info["faces"]:
        print(face)

detect_emotion("http://farm1.staticflickr.com/1/39961_a75792f7ec.jpg")