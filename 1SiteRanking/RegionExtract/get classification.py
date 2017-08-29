#按userid分组后组内排序，取出每组最大最小值

import psycopg2
#链接到我的PostgreSQL数据库
connection = psycopg2.connect(database="postgres", user="postgres", host="127.0.0.1", port='5432', password="kwy17502X")
print(1)
#获取游标
cursor = connection.cursor()
print(2)

try:
    # 修改表名
    cursor.execute("CREATE TABLE classify_4 (id serial PRIMARY KEY, userid text , time text);")
    print(3)

    #打开数据文件
    file = open('C:/Users/Administrator/Desktop/countphototime.txt')

    lines = file.readlines()
    file.close()
    print(4)
    for line in lines:
        line = line.split('\t')
        print(line[0])
        # 修改表名
        cursor.execute("INSERT INTO classify_4 (userid,time) VALUES (%s,%s)", (line[0],line[1]))
     # 修改表名
    cursor.execute("copy (select userid,time from (select userid,time,ROW_NUMBER() over(partition by userid order by time DESC) as new_index from classify_4) a where a.new_index=1) to 'E:/max.txt' with csv;")
    print(5)
    # 修改表名
    cursor.execute("copy (select userid,time from (select userid,time,ROW_NUMBER() over(partition by userid order by time ) as new_index from classify_4) a where a.new_index=1) to 'E:/min.txt' with csv;")
    print(6)
    #修改表名
  #  cursor.execute("copy(select (select time as max from (select time,ROW_NUMBER() over(partition by userid order by time DESC) as new_index from classify_4) a where a.new_index=1),(select time as min from (select time,ROW_NUMBER() over(partition by userid order by time) as new_index from classify_4) a where a.new_index=1) from classify_4) to 'E:/union.txt' with csv;")
except Exception as e:
    print(repr(e))

connection.commit()
connection.close()

