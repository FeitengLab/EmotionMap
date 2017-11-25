def three_word(a, b, c):
    title = a
    if title == '\"\"':
        title = "\'\'"
    else:
        title = "\'{0}\'".format(title)
    tag = b
    if tag == '\"\"':
        tag = "\'\'"
    else:
        tag = "\'{0}\'".format(tag)
    description = c
    if description == '\"\"':
        description = "\'\'"
    else:
        description = "\'{0}\'".format(description)
    return title, tag, description


def format_file(old_file, new_file):
    try:
        format_file = open(new_file, 'a')
        with open(old_file, 'r') as face_file:
            for line in face_file:
                line = line.split('\n')[0]
                title, tag, description = three_word(line.split('\t')[4], line.split('\t')[5], line.split('\t')[6])
                face_data = "{0},\'{1}\',\'{2}\',{3},{4},{5},{6}," \
                            "{7},{8},{9},\'{10}\',{11},{12},{13},{14},{15},{16}," \
                            "{17},{18},{19},{20},{21},{22},{23},{24},{25}\n" \
                    .format(line.split('\t')[0],
                            line.split('\t')[1], line.split('\t')[2],
                            line.split('\t')[3], title, tag, description,
                            line.split('\t')[7], line.split('\t')[8],
                            line.split('\t')[9], line.split('\t')[10],
                            line.split('\t')[11], line.split('\t')[12],
                            line.split('\t')[13], line.split('\t')[14],
                            line.split('\t')[15], line.split('\t')[16],
                            line.split('\t')[17], line.split('\t')[18],
                            line.split('\t')[19],
                            line.split('\t')[20], line.split('\t')[21],
                            line.split('\t')[22], line.split('\t')[23],
                            line.split('\t')[24], line.split('\t')[25])
                format_file.writelines(face_data)
        format_file.close()
    except Exception as e:
        with open('log.txt', 'a') as log:
            log.writelines("{0},{1}".format(new_file, e))


if __name__ == '__main__':
    start = 3
    end = 135
    for i in range(start, end):
        print(i)
        format_file(r'D:\Users\KYH\Desktop\EmotionMap\FlickrEmotionData\4face_all\face{0}.txt'.format(i),
                    r'D:\Users\KYH\Desktop\EmotionMap\FlickrEmotionData\5face_format\face{0}.txt'.format(i))
