# coding:utf-8
# version:python3.5.1
# author:kyh
# import geodata csv files to cloud database

import psycopg2


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

    # Export tables
    # 导出表
    def export_table(self, start, end):
        for i in range(start, end):
            try:
                sql_command = '''
                COPY public.face{0} (id,longitude,latitude,faceid)
                TO 'D:\\Users\\KYH\\Desktop\\EmotionMap\\FlickrEmotionData\\6face_pt\\facept{0}.txt' DELIMITER ',';
            '''.format(i)
                self.cursor.execute(sql_command)
                self.connection.commit()
            except Exception as e:
                self.write_log(e)


if __name__ == '__main__':
    try:
        # 连接数据库
        # database = CloudDatabase("Face", "postgres", "postgres", "47.89.209.207")
        # 连接本地数据库
        database = CloudDatabase("Face", "postgres", "postgres", "127.0.0.1")
        database.db_connect()
        # 创建照片表
        # start指的是从第几个数据库表开始end表示的是第几个数据库表结束
        start = 1
        end = 135
        database.export_table(start, end)
        # 导入csv数据
    except Exception as e:
        with open("log.txt", 'a') as log_file:
            log_file.writelines(str(e))
