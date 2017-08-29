#分别得到min,max和Union三个含有时间的txt
import psycopg2
#链接到我的PostgreSQL数据库
connection = psycopg2.connect(database="postgres", user="postgres", host="127.0.0.1", port='5432', password="kwy17502X")
print(1)
#获取游标
cursor = connection.cursor()
print(2)

try:
    cursor.execute("drop table min")
    cursor.execute("drop table max")
#    cursor.execute("drop table uniontime")
    cursor.execute("CREATE TABLE min (id serial PRIMARY KEY, userid text ,  min text);")
    print(3)
    cursor.execute("CREATE TABLE max (id serial PRIMARY KEY, userid text ,  max text);")
    print(4)

    #将max导入数据库
    filemax = open('E:/max.txt')
    linesmax = filemax.readlines()
    filemax.close()
    numbermax=1
    for linemax in linesmax:
        if(numbermax%2):
            linemax = linemax.split(',')
            linemax[1]=linemax[1].replace('\"','')
            print(linemax[0])
        # 修改表名
            cursor.execute("INSERT INTO max (userid,max) VALUES (%s,%s)", (linemax[0],linemax[1]))
        numbermax=numbermax+1

    #将min导入数据库
    filemin = open('E:/min.txt')
    linesmin = filemin.readlines()
    filemin.close()
    numbermin = 1
    for linemin in linesmin:
        if (numbermin % 2):
            linemin = linemin.split(',')
            linemin[1] = linemin[1].replace('\"', '')
            print(linemin[0])
            # 修改表名
            cursor.execute("INSERT INTO min (userid,min) VALUES (%s,%s)", (linemin[0], linemin[1]))
        numbermin = numbermin + 1

    #导出union结果到union.txt
    cursor.execute("copy(SELECT max.userid, max.max,min.min FROM max INNER JOIN min ON max.userid=min.userid ) to 'E:/union.txt' with csv;")
    #将结果存入数据库——未完成

# cursor.execute("CREATE TABLE uniontime (id serial PRIMARY KEY , userid text , maxtime text , mintime text);")
 #   numberunion=0
 #   fileunion = open('E:/union.txt')
  #  linesunion = fileunion.readlines()
 #   fileunion.close()
  #  numberunion = 1
 #   for lineunion in linesunion:
     #   lineunion=lineunion.replace('\"','')
     #   lineunion = lineunion.replace('\n', '')
  #      lineunion = lineunion.split(',')
  #      print(lineunion)
  #      print(133)
  #      if ((numberunion % 3)==1):

            # 修改表名
   #         numberunion = numberunion + 1
   #         cursor.execute("INSERT INTO uniontime (userid,maxtime) VALUES (%s,%s,%s)", (lineunion[0], str(lineunion[1])))

    #    if ((numberunion % 3)==2):
    #        # 修改表名
    #        numberunion = numberunion + 1
    #        cursor.execute("INSERT INTO uniontime (mintime) VALUES (%s)", (str(lineunion[1]),))

    #    if ((numberunion % 3)==0):
     #       numberunion = numberunion + 1

except Exception as e:
    print(repr(e))

connection.commit()
connection.close()
