# coding:utf-8
# version:python3.6.0
# author:zxh,kyh
# extract emotion from photo to face

import json


# 输入：列表中的情绪字符串 输出：包含多个人的情绪列表
def decode_json(json_str):
    # 将字符串转化为 json.loads() 可加载的对象
    json_str = json_str.replace('""', "|")
    json_str = json_str.replace('"', '')
    json_str = json_str.replace('|', '"')

    l = json.loads(json_str)
    return l


# 输入：单个人的情绪字典（包含8种情绪指标） 输出：情绪指数csv（字符串）
def dict2csv(emotion_d):
    # 情绪字典转化为情绪指数列表
    emotion_score = []
    for i in emotion_d:
        emotion_score.append(str(emotion_d[i]))

    # 情绪指数列表转化为情绪指数csv
    emotion_csv = ",".join(emotion_score)
    return emotion_csv


def write_faces(file_source_path,file_result_path):
    with open(file_source_path, 'r') as f_source:
        with open(file_result_path, 'a') as f_result:
            # 逐行读取数据并转化为列表，列表中的元素均为字符串
            for line_source in f_source.readlines():
                line_list = line_source.split('\t')

                # line_list[11] 是 facenum 那一列，line_list[12] 是 emotion 那一列
                if ((line_list[11] != 'facenum') and (line_list[11] != '0')):
                    l = decode_json(line_list[12])
                    # 将每一张脸的8大情绪指数转化为csv，并创建一行数据
                    for j in l:
                        emotion_d = j["emotion"]
                        emotion_csv = dict2csv(emotion_d)
                        line_list[12] = emotion_csv
                        line_result = "\t".join(line_list)
                        f_result.write(line_result + '\n')

if __name__ == '__main__':
    for i in range(0,26):
        write_faces('flickr{0}.txt'.format(i),'faceflickr{0}.txt'.format(i))

