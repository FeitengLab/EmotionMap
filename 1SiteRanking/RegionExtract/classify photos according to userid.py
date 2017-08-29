#将userid,photoid,x,y坐标存储进数据库成为单张表，并且得到按userid统计的每个user所发照片数量的txt
import psycopg2

#链接到我的PostgreSQL数据库
connection = psycopg2.connect(database="postgres", user="postgres", host="127.0.0.1", port='5432', password="kwy17502X")
print(1)
#获取游标
cursor = connection.cursor()
print(2)

try:
#    cursor.execute("case when t=(select count(*) from classify_3)  then  drop table classify_3 ")
    #修改表名
    cursor.execute("CREATE TABLE classify_3 (id serial PRIMARY KEY, photoid text , userid text , x text , y text);")
    print(3)

    #打开数据文件
    file = open('C:/Users/Administrator/Desktop/countnumber.txt')

    lines = file.readlines()
    file.close()
    print(4)
    for line in lines:
        line = line.split('\t')
        print(line[0])
        # 修改表名
        cursor.execute("INSERT INTO classify_3 (photoid,userid,x,y) VALUES (%s,%s,%s,%s)", (line[0],line[1],line[2],line[3]))
        #导出表
        # 修改表名
        cursor.execute("copy classify_3 to 'E:/table.txt' with csv;")
        # 修改表名
        cursor.execute("copy (select userid,count(*) AS number from classify_3 group by userid) to 'E:/count.txt' with csv;")
except Exception as e:
    print(repr(e))

connection.commit()
connection.close()

