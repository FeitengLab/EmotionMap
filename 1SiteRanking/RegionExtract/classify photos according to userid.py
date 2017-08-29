# coding:utf-8
# version:python3.5.1
# author:kwy
# calculate the number of photo uploaded of each user
# 将userid,photoid,x,y坐标存储进数据库成为单张表，并且得到按userid统计的每个user所发照片数量的txt
import psycopg2


# 链接到我的PostgreSQL数据库
def db_connect():
    connection = psycopg2.connect(database="postgres", user="postgres", host="127.0.0.1", port='5432',
                                  password="kwy17502X")
    print(1)
    # 获取游标
    cursor = connection.cursor()
    print(2)
    return connection, cursor


# 关闭数据库
def db_close(connection):
    connection.close()


if __name__ == '__main__':
    filepath = "C:/Users/Administrator/Desktop/countnumber.txt"
    try:
        connection, cursor = db_connect()
        # 创建表
        sql_create_table = "CREATE TABLE classify_3 (id serial PRIMARY KEY, photoid text , userid text , x text , y text);"
        cursor.execute(sql_create_table)
        print(3)
        # 打开数据文件
        file = open(filepath, 'r')
        lines = file.readlines()
        file.close()
        print(4)
        for line in lines:
            line = line.split('\t')
            print(line[0])

            # 将数据插入表中
            sql_insert = "INSERT INTO classify_3 (photoid,userid,x,y) VALUES (%s,%s,%s,%s)", (
                line[0], line[1], line[2], line[3])
            cursor.execute(sql_insert)

            # 将数据导出
            sql_export = "copy classify_3 to 'E:/table.txt' with csv;"
            cursor.execute(sql_export)

            # 统计人数
            sql_user = "copy (select userid,count(*) AS number from classify_3 group by userid) to 'E:/count.txt' with csv;"
            cursor.execute(sql_user)
            print(5)

            # 关闭
        connection.commit(cursor)
        connection.close()
    except Exception as e:
        print(repr(e))
