# coding:utf-8
# version:python3.5.1
# author:kyh
# export geodata from cloud database to local csv files

import psycopg2

connection = psycopg2.connect(database="Flickr1", user="postgres",
                                   password="postgres", host="127.0.0.1", port="5432")
cursor = connection.cursor()
sql_command="SELECT * FROM flickr0"
cursor.execute(sql_command)
count=0
f=open('test.csv','a')
for data in cursor.fetchall():
    f.write(str(data))
    f.write('\n')
f.close()
f=open('test.csv','r')
print(f.readline())
