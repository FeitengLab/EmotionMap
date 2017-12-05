# coding:utf-8
# version:python3.5.1
# author:kyh
# execute sql command
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

    # 将数据导入
    def execute_sql(self):
        try:
            sql_command = '''
                CREATE INDEX iface_lon ON face(longitude);
CREATE INDEX iface_lat ON face(latitude);

CREATE INDEX iface_id ON face(id);
CREATE INDEX iface_userid ON face(userid);
CREATE INDEX iface_photo_date_taken ON face(photo_date_taken);
CREATE INDEX iface_facenum ON face(facenum);
CREATE INDEX iface_happiness ON face(happiness);
CREATE INDEX iface_neutral ON face(neutral);
CREATE INDEX iface_sadness ON face(sadness);
CREATE INDEX iface_disgust ON face(disgust);
CREATE INDEX iface_anger ON face(anger);
CREATE INDEX iface_fear ON face(fear);
CREATE INDEX iface_surprise ON face(surprise);
CREATE INDEX iface_smile_s ON face(smile_s);
CREATE INDEX iface_smile_v ON face(smile_v);
CREATE INDEX iface_gender ON face(gender);
CREATE INDEX iface_ethnicity ON face(ethnicity);
CREATE INDEX iface_age ON face(age);

CREATE INDEX iface_pt ON face(point) USING gist(Point);
				'''
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
        # 说明做什么
        print_log = "create index"
        print(print_log)
        # 执行SQL语句
        database.create_table(start, end)
        # 结束
        print("End!", print_log)
    except Exception as e:
        with open("log.txt", 'a') as log_file:
            log_file.writelines(str(e))
