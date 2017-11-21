# coding:utf-8
# version:python3.6.0
# author:kyh
# split all files into small files

# 将所有的数据保存到一个文件中
def read_files():
    with open('faceall.txt', 'a') as allfile:
        for i in range(26):
            if (i is 5) or (i is 22) or (i is 25):
                continue
            with open('faceflickr{0}.txt'.format(i), 'r') as file:
                print(i)
                for face in file.readlines():
                    allfile.writelines(face)


# 将大文件拆分
def write_files():
    file = open('faceall.txt', 'r')
    face_file = open('face0.txt', 'a')
    face = file.readline()
    i = 0
    while face is not None:
        i = i + 1
        if i % 100000 is 0:
            print(int(i / 100000))
            face_file.close()
            face_file = open('face{0}.txt'.format(int(i / 100000)), 'a')
        face_file.writelines(face)
        face = file.readline()
    face_file.close()


# 判断是否有缺失
def files_compute():
    all_count = 0
    with open('faceall.txt', 'r') as all_file:
        for face in all_file.readlines():
            all_count = all_count + 1
    print(all_count)
    all_count = 0
    for i in range(0, 120):
        print(i)
        with open('face{0}.txt'.format(i), 'r') as face_file:
            for face in face_file.readlines():
                all_count = all_count + 1
    print(all_count)


if __name__ == '__main__':
    # read_files()
    # write_files()
    files_compute()
