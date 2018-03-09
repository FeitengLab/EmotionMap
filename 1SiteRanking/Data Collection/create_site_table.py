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

    # Copy files to database
    # 将csv文件导入数据库
    def import_site(self, filepath):
        with open(filepath,'r') as file:
            for site in file.readlines():
                id = site.split('\t')[0]
                name = site.split('\t')[1]
                lat = site.split('\t')[2]
                lon = site.split('\t')[3].split('\n')[0]
                try:
                    sql_command="INSERT INTO site VALUES ({0},'{1}',{2},{3});".format(id,name,lat,lon)
                    self.cursor.execute(sql_command)
                    self.connection.commit()
                except Exception as e:
                    self.write_log(e)


if __name__ == '__main__':
    try:
        # 连接本地数据库
        database = CloudDatabase("EmotionMap3", "postgres", "postgres", "127.0.0.1")
        database.db_connect()
        database.import_site(r'site_info.txt')
    except Exception as e:
        with open("log.txt", 'a') as log_file:
            log_file.writelines(str(e))