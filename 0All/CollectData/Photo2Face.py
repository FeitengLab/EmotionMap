# coding:utf-8
# version:python3.6.0
# author:zxh,kyh
# extract emotion from photo to face

import json


# 输入：face++_API 返回的人脸属性 输出：以人脸为单位的属性列表
def decode_json(faces_str):

    # 将 faces_str 转化为 json.loads() 可加载的对象
    faces_str = faces_str.replace('""', "|")
    faces_str = faces_str.replace('"', '')
    faces_json = faces_str.replace('|', '"')

    faces_l = json.loads(faces_json)
    return faces_l


# 输入：单张脸的属性 输出：'[7个情绪值], [其他属性值]'
def dict2csv(single_face):
    face_list = []

    # 按照'happiness', 'neutral', 'sadness', 'disgust', 'anger', 'fear', 'surprise' 的顺序添加情绪指数
    emotion = single_face['emotion']
    face_list.append(str(emotion['happiness']))
    face_list.append(str(emotion['neutral']))
    face_list.append(str(emotion['sadness']))
    face_list.append(str(emotion['disgust']))
    face_list.append(str(emotion['anger']))
    face_list.append(str(emotion['fear']))
    face_list.append(str(emotion['surprise']))

    # 添加 facequality 和 smile 的阈值和值
    facequality = single_face['facequality']
    face_list.append(str(facequality['threshold']))
    face_list.append(str(facequality['value']))

    smile = single_face['smile']
    face_list.append(str(smile['threshold']))
    face_list.append(str(smile['value']))

    # 添加 gender：'Male'->0; 'Female'->1
    gender = single_face['gender']['value']
    if gender == 'Male':
        face_list.append('0')
    else:
        face_list.append('1')

    # 添加 ethnicity：'Asian'->0; 'White'->1; 'Black'->2
    ethnicity = single_face['ethnicity']['value']
    if ethnicity == 'Asian':
        face_list.append('0')
    elif ethnicity == 'White':
        face_list.append('1')
    else:
        face_list.append('2')

    # 添加 age
    age = single_face['age']['value']
    face_list.append(str(age))

    return face_list


def write_faces(file_source_path, file_result_path):
    with open(file_source_path, 'r') as f_source:
        with open(file_result_path, 'a') as f_result:
            data_count = 0
            has_faces_count = 0
            face_count = 0

            # 逐行读取数据并转化为列表
            for line_source in f_source.readlines():
                line_base = line_source.split('\t')
                if len(line_base) > 11:  # 排除没有数据的行
                    data_count = data_count + 1

                    # line_list[11]: facenum；line_list[12]：attribute
                    if (line_base[11] != 'facenum') and (line_base[11] != '0') and (len(line_base) == 13):
                        face_l = decode_json(line_base[12])
                        has_faces_count = has_faces_count + 1
                        del line_base[12]

                        # 将单张人脸属性转化为特定格式并写入一行数据
                        for face in face_l:
                            face_list = dict2csv(face)
                            line_result = line_base + face_list
                            line_result = "\t".join(line_result)
                            f_result.write(line_result + '\n')
                            face_count = face_count + 1
                            # print(line_source)
                            # print(line_result)

            counts = [file_source_path, str(data_count), str(has_faces_count), str(face_count)]
            # print(counts)
            return counts


if __name__ == '__main__':
    # 输出
    with open('counts_summary.txt', 'a') as f:
        f.write("filename\tdata_count\thas_faces_count\tface_count\n")
    for i in range(0, 26):
        counts = write_faces('flickr{0}.txt'.format(i),'faceflickr{0}.txt'.format(i))
        with open('counts_summary.txt', 'a') as f:
            line = "\t".join(counts)
            f.write(line+'\n')
