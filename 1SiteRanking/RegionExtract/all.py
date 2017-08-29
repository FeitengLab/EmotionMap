# coding:utf-8
# version:python3.5.1
# author:kwy
# import geodata csv files to cloud database
import os.path
from collections import Counter


class data:
    datacount = 0

    def __init__(self, photoid, userid, taketime, uploadtime, title, description, geotag, lon, lat, accuracy, url):
        self.photoid = photoid
        self.userid = userid
        self.taketime = taketime
        self.uploadtime = uploadtime
        self.title = title
        self.description = description
        self.geotag = str(geotag)
        self.lon = lon
        self.lat = lat
        self.accuracy = accuracy
        self.url = url
        data.datacount += 1

    def tag_wash(self):
        words=['\n',' ','+']
        for word in words:
            self.geotag=self.geotag.replace(word,'')

        self.geotag = self.geotag.lower()
        self.geotag = self.geotag.replace('\'', '')
        self.geotag = self.geotag.replace(' ', '')
        self.geotag = self.geotag.replace('+', '')
        self.geotag = self.geotag.replace('_', '')
        self.geotag = self.geotag.replace('-', '')
        self.geotag = self.geotag.replace('%', '')
        self.geotag = self.geotag.replace('0', '')
        self.geotag = self.geotag.replace('9', '')
        self.geotag = self.geotag.replace('8', '')
        self.geotag = self.geotag.replace('7', '')
        self.geotag = self.geotag.replace('6', '')
        self.geotag = self.geotag.replace('5', '')
        self.geotag = self.geotag.replace('4', '')
        self.geotag = self.geotag.replace('3', '')
        self.geotag = self.geotag.replace('2', '')
        self.geotag = self.geotag.replace('1', '')
        # 读取每一行数据，存储到list[i]里

try:
    rootdir = "H:\emotion\sites"
    for parent, dirnames, filenames in os.walk(rootdir):
        for dirname in dirnames:  # 输出文件夹信息
            print("parent is:" + parent)
            print("dirname is" + dirname)

        for filename in filenames:  # 输出文件信息
            print(filenames)
            print("parent is:" + parent)
            print("filename is:" + filename)
            print("the full name of the file is:" + os.path.join(parent, filename))  # 输出文件路径信息
            path = os.path.join(parent, filename)
            list = []
            number = 0

            with open(path, 'r') as fd:
                for line in fd:
                    line = line.split('\t')
                    #  if line[7].strip() != '':
                    if len(line) == 11:
                        instance = data(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8],
                                        line[9], line[10])
                        list.append(instance)
                        number = number + 1
                        print(instance.lon)
            print(number)

            # 数据存储完毕，list里共有number条记录

            # 对list[i]的geotag进行处理
            listgeotag = []
            list_geotag_string = []
            for i in range(0, number):
                list[i].geotag = list[i].geotag.lower()
                list[i].geotag = list[i].geotag.replace('\'', '')
                list[i].geotag = list[i].geotag.replace(' ', '')
                list[i].geotag = list[i].geotag.replace('+', '')
                list[i].geotag = list[i].geotag.replace('_', '')
                list[i].geotag = list[i].geotag.replace('-', '')
                list[i].geotag = list[i].geotag.replace('%', '')
                list[i].geotag = list[i].geotag.replace('0', '')
                list[i].geotag = list[i].geotag.replace('9', '')
                list[i].geotag = list[i].geotag.replace('8', '')
                list[i].geotag = list[i].geotag.replace('7', '')
                list[i].geotag = list[i].geotag.replace('6', '')
                list[i].geotag = list[i].geotag.replace('5', '')
                list[i].geotag = list[i].geotag.replace('4', '')
                list[i].geotag = list[i].geotag.replace('3', '')
                list[i].geotag = list[i].geotag.replace('2', '')
                list[i].geotag = list[i].geotag.replace('1', '')
                #  print(list[i].geotag)

                # geotag特殊字符替换完毕，大写转换为小写转换完毕

                list_geotag_string.append(str(list[i].geotag))
                list_geotag_string[i] = list_geotag_string[i].split(',')
                # geotag存储为字符形式,按照','分列

                # 将每一个geotag按,分列，所有的分列后的geotag放进同一个数组listgeotag

                splitgeotag = list[i].geotag.split(',')
                for section in splitgeotag:
                    listgeotag.append(section)
            print(listgeotag)
            # 存储完毕
            # 统计geotag词频
            frequency = Counter(listgeotag)
            print(frequency)
            frequency_string = str(frequency)
            frequency_string = frequency_string.split(',')

            # 文件夹创建和存入
            os.chdir(r'E:/emotion/')
            name = filename[:-4]
            print("Received input is : ", name)
            # retval = os.getcwd()[:0]+'tajmahal\\'
            retval = os.getcwd()[:0] + name + "\\"
            if not os.path.exists(retval):
                os.makedirs(retval)
            os.chdir(retval)
            print(retval)
            # 文件夹创建和存入完毕
            for one in frequency_string:
                #   filefrequency = open('C:/Users/Administrator/Desktop/geotagfrequency.txt', 'a+')
                filefrequency = open('geotagfrequency.txt', 'a+')
                filefrequency.write(str(one) + '\n')
                filefrequency.close()

                # 词频统计完毕，结果存储在frequency中；导出文件为geotagfrequency

                # 注意！！！词频需要手动选择！！！！！！！

                # 按照主观选择的geotag筛选记录
                # 所选筛选词
                #  geotag_aim='tajmahal'
            geotag_aim = input("Enter your input: ")
            print("Received input is : ", geotag_aim)

            filterdata = []
            count = 0
            for j in range(0, number):
                if geotag_aim in list_geotag_string[j]:
                    filterdata.append(list[j])
                    count = count + 1
                    #   filefilter = open('C:/Users/Administrator/Desktop/location.txt', 'a+')
                    filefilter = open('location.txt', 'a+')
                    filefilter.write('lat' + '\t' + 'lon' + '\n')
                    filefilter.write(str(list[j].lat) + '\t' + str(list[j].lon) + '\n')
                    filefilter.close()

                    # dbscan的input数据的csv形式
                    #   filedbscan = open('C:/Users/Administrator/Desktop/dbscaninput.txt', 'a+')
                    filedbscan = open('dbscaninput.txt', 'a+')
                    filedbscan.write('photoid' + '\t' + 'userid' + '\t' + 'x' + '\t' + 'y' + '\n')
                    list[j].userid = list[j].userid.replace('\'', '')
                    filedbscan.write(
                        str(list[j].photoid) + ',' + str(list[j].userid) + ',' + str(list[j].lon) + ',' + str(
                            list[j].lat) + '\n')
                    filedbscan.close()

                    # 按userid统计的每个user所发照片数量的txt的原始数据
                    #   filecountnumber = open('C:/Users/Administrator/Desktop/countnumber.txt', 'a+')
                    filecountnumber = open('countnumber.txt', 'a+')
                    #   filecountnumber.write('userid' + '\t' + 'photoid' + '\t' + 'lon' + '\t' + 'lat' + '\n')
                    filecountnumber.write(
                        str(list[j].photoid) + '\t' + str(list[j].userid) + '\t' + str(list[j].lon) + '\t' + str(
                            list[j].lat) + '\n')
                    filecountnumber.close()

                    # 到每个用户所发照片的最早和最晚时间的两个txt的原始数据
                    #   filecounttime = open('C:/Users/Administrator/Desktop/countphototime.txt', 'a+')
                    filecounttime = open('countphototime.txt', 'a+')
                    # filecounttime.write('userid' + '\t' + 'taketime' + '\n')
                    list[j].taketime = list[j].taketime.replace('\'', '')
                    filecounttime.write(str(list[j].userid) + '\t' + str(list[j].taketime) + '\n')
                    filecounttime.close()
            print(count)




except Exception as e:
    print(repr(e))
