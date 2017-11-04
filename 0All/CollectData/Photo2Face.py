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

    # 情绪字典转化为情绪指数列表
    emotion_score = []
    for emotion in single_face['emotion']:
        emotion_score.append(single_face['emotion'][emotion])

    # 其余属性汇总成列表
    remain_l = []
    del single_face['emotion']
    for i in single_face:
        for j in single_face[i]:
            remain_l.append(single_face[i][j])

    # 'Male'->0; 'Female'->1
    if remain_l[-3] == 'Male':
        remain_l[-3] = 0
    else:
        remain_l[-3] = 1

    # 'Asian'->0; 'White'->1; 'Black'->2
    if remain_l[-1] == 'Asian':
        remain_l[-1] = 0
    elif remain_l[-1] == 'White':
        remain_l[-1] = 1
    else:
        remain_l[-1] = 2

    face_csv = ",".join([str(emotion_score), str(remain_l)])

    return face_csv


def write_faces(file_source_path, file_result_path):
    with open(file_source_path, 'r') as f_source:
        with open(file_result_path, 'a') as f_result:
            data_count = 0
            has_faces_count = 0
            face_count = 0

            # 逐行读取数据并转化为列表
            for line_source in f_source.readlines():
                line_list = line_source.split('\t')
                if len(line_list) > 11:    # 排除没有数据的行
                    data_count = data_count + 1

                # line_list[11]: facenum；line_list[12]：attribute
                    if (line_list[11] != 'facenum') and (line_list[11] != '0') and (len(line_list) == 13):
                        face_l = decode_json(line_list[12])
                        has_faces_count = has_faces_count + 1

                        # 将单张人脸属性转化为特定格式并写入一行数据
                        for face in face_l:
                            face_csv = dict2csv(face)
                            line_list[12] = face_csv
                            line_result = "\t".join(line_list)
                            f_result.write(line_result + '\n')
                            face_count = face_count + 1

            counts = [file_source_path, str(data_count), str(has_faces_count), str(face_count)]
            print(counts)
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
