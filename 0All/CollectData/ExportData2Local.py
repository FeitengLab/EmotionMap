# coding:utf-8
# version:python3.5.1
# author:kyh
# export geodata from cloud database to local csv files

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


    # Export data to local files
    # 将云端数据库中的数据导出为本地文件
    def export_db2local(self,filepath,start,end):
        for i in range(start,end):
            print(i)
            try:
                # 打开文件
                file = open("{0}\\{1}.csv".format(filepath, i), 'a')
                sql_command="SELECT * FROM flickr{0} WHERE facenum>0".format(i)






if __name__ == '__main__':
    try:
        # 连接数据库
        database = CloudDatabase("Flickr1", "postgres", "postgres", "47.89.209.207")
        # 连接本地数据库
        # database = CloudDatabase("Flickr1", "postgres", "postgres", "127.0.0.1")
        database.db_connect()
    except Exception as e:
        with open("log.txt", 'a') as log_file:
            log_file.writelines(str(e))
