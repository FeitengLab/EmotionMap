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
    def import_csv2db(self, filepath, start, end):
        for i in range(start, end):
            print(i)
            try:
                # 打开文件
                file = open("{0}\\face{1}.txt".format(filepath, i), 'r')
                line = file.readline()
                # 起始的SQL语句
                sql_command = "INSERT INTO face{0} VALUES (".format(i)
                # 计数
                count = 1
                while line:
                    # 构造SQL语句
                    line = line.replace('\t', ',')
                    sql_command += "{0}),(".format(line.split('\n')[0])
                    # 如果是10000的倍数则提交
                    if count % 10000 == 0:
                        print("{0},{1}".format(i, count))
                        sql_command = sql_command[:-2]
                        # 提交数据
                        self.cursor.execute(sql_command)
                        self.connection.commit()
                        # 构造新的SQL语句
                        sql_command = "INSERT INTO face{0} VALUES (".format(i)
                    count += 1
                    # 读取下一条数据
                    line = file.readline()
                # 全部跑完则将剩余的数据提交
                sql_command = sql_command[:-2]
                self.cursor.execute(sql_command)
                self.connection.commit()
            except Exception as e:
                self.write_log(e)

    # Create tables
    # 创建表
    def create_table(self, start, end):
        for i in range(start, end):
            try:
                sql_command = '''
                CREATE TABLE face{0}
                (id BIGINT NOT NULL,
                userid TEXT,
                photo_date_taken DATE,
                photo_date_uploaded BIGINT,
                title TEXT DEFAULT NULL,
                description TEXT DEFAULT NULL,
                user_tags TEXT DEFAULT NULL,
                longitude FLOAT DEFAULT 0,
                latitude FLOAT DEFAULT 0,
                accuracy INTEGER DEFAULT 0,
                download_url TEXT NOT NULL,
                facenum INTEGER,
                happiness FLOAT,
                neutral FLOAT,
                sadness FLOAT,
                disgust FLOAT,
                anger FLOAT,
                fear FLOAT,
                surprise FLOAT,
                facequality_s FLOAT,
                facequality_v FLOAT,
                smile_s FLOAT,
                smile_v FLOAT,
                gender INTEGER,
                ethnicity INTEGER,
                age INTEGER,
                faceid serial PRIMARY KEY 
                );
                CREATE INDEX iface_id{0} ON face{0}(id);
                CREATE INDEX iface_date{0} ON face{0}(photo_date_taken);
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
        start =1
        end = 135
        database.create_table(start, end)
        # 导入csv数据
        database.import_csv2db(r"D:\Users\KYH\Desktop\EmotionMap\FlickrEmotionData\5face_format", start, end)
    except Exception as e:
        with open("log.txt", 'a') as log_file:
            log_file.writelines(str(e))
