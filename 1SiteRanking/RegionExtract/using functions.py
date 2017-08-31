import os
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
        self.geotag = geotag
        self.lon = lon
        self.lat = lat
        self.accuracy = accuracy
        self.url = url
        data.datacount += 1


def storage(path, list):
    # 读取每一行数据，存储到list[i]里
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
    # 因为你使用了with as的表达所以不需要再close了
    # fd.close()
    print(number)
    # 数据存储完毕，list里共有number条记录
    return number


def geotagpro(list, listgeotag, list_geotag_string, number):
    # 对list[i]的geotag进行处理
    words = ['\'', ' ', '+', '_', '-']
    for i in range(0, number):
        list[i].geotag = list[i].geotag.lower()
        for word in words:
            list[i].geotag = list[i].geotag.replace(word, '')
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

        # geotag存储为字符形式,按照','分列
        list_geotag_string.append(str(list[i].geotag))
        list_geotag_string[i] = list_geotag_string[i].split(',')
        # geotag存储为字符形式,按照','分列

        # 将每一个geotag按,分列，所有的分列后的geotag放进同一个数组listgeotag
        splitgeotag = list[i].geotag.split(',')
        for section in splitgeotag:
            listgeotag.append(section)
    return


def geofrequency(listgeotag):
    # 统计geotag词频
    frequency = Counter(listgeotag)
    print(frequency)
    frequency_string = str(frequency)
    frequency_string = frequency_string.split(',')

    return frequency_string


def creatfile(filename):
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

    return
    # 文件夹创建和存入完毕


def writefrequency(frequency_string):
    for one in frequency_string:
        #   filefrequency = open('C:/Users/Administrator/Desktop/geotagfrequency.txt', 'a+')
        filefrequency = open('geotagfrequency.txt', 'a+')
        filefrequency.write(str(one) + '\n')
        filefrequency.close()

        return
        # 词频统计完毕，结果存储在frequency中；导出文件为geotagfrequency


def filtergeotag():
    # 获取用户输入的geotag筛选词
    geotag_aim = input("Enter your input: ")
    print("Received input is : ", geotag_aim)

    return geotag_aim


def writealltxt(geotag_aim, list_geotag_string, number, list):
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
            filedbscan.write("{0},{1},{2},{3}\n".format(list[j].photoid, list[j].userid, list[j].lon, list[j].lat))
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

    return


# 主函数
if __name__ == '__main__':
    try:
        # 遍历文件夹内所有文件
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

                # 函数引用

                # 读取每一行数据，存储到list[i]里
                list = []
                number = storage(path, list)
                # 数据存储完毕，list里共有number条记录

                # 对list[i]的geotag进行处理
                # 将每一个geotag替换特殊字符，按,分列，所有的分列后的geotag放进同一个数组listgeotag
                listgeotag = []
                list_geotag_string = []
                geotagpro(list, listgeotag, list_geotag_string, number)

                # 统计geotag词频
                frequency_string = geofrequency(listgeotag)

                # 文件夹创建和存入
                creatfile(filename)

                # 词频统计导出文件为geotagfrequency
                writefrequency(frequency_string)

                # 获取用户输入的geotag筛选词
                geotag_aim = filtergeotag()

                # 获得dbscan的input数据的csv形式，以及其余两个也许用得到的csv文件，具体注释在相应函数里
                writealltxt(geotag_aim, list_geotag_string, number, list)

    except Exception as e:
        print(repr(e))
