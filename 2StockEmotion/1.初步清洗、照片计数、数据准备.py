
# coding: utf-8

# In[4]:


from os.path import splitext


# In[7]:


def file_add_suffix(filename, suffix):
    fn, ext = splitext(filename)
    return fn + suffix + ext


def file_replace_suffix(filename, old_suf, new_suf):
    fn, ext = splitext(filename)
    return fn.replace(old_suf, new_suf) + ext


# In[ ]:


def wash1(filename):
    """The first step of wash.
    Input: processing the file retrieved from PostgreSQL, which separates 
    items with | and space.
    Output: a washed file separated with Tab.
    Return: the name of output file.

    主要是将空格， | 去除，转换为简单的CSV格式，用Tab隔开"""
    new_file = file_add_suffix(filename, '1')
    with open(filename) as f, open(new_file, 'w', encoding='utf-8') as g:
        for line in f:
            l = line.split('|')
            l = [i.strip() for i in l]
            g.write('\t'.join(l) + '\n')
    return new_file


#

def wash2(filename):
    """The second step of wash.
    Input: result file of wash1()

    Output:  a washed file
    Return: the name of output file

    将coordinates 分为 lat 和 lon"""
    new_file = file_replace_suffix(filename, '1', '2')
    with open(filename) as f, open(new_file, 'w', encoding='utf-8') as g:
        for line in f:
            l = line.split('\t')
            l = [i.strip() for i in l]
            try:
                coordinates = l.pop(2)
            except:
                print(repr(line))  # 最后一行的问题没有写入新文件，很舒服
                continue
            coordinates = coordinates.replace('(', '').replace(')', '')
            if ',' in coordinates:
                coor = coordinates.replace(',', '\t')
            else:
                coor = 'lat\tlon'
            l.append(coor)
            g.write('\t'.join(l) + '\n')
    return new_file


#  将文件分离为Tokyo.txt 和 London.txt 



with open('TokyoAndLondon2.txt') as f, open('Tokyo.txt', 'w', encoding='utf-8') as g, open('London.txt', 'w', encoding='utf-8') as h:
    for line in f:
        l = line.split('\t')
        l = [i.strip() for i in l]
        site = l.pop(0)
        if site == 'site':
            g.write('\t'.join(l) + '\n')
            h.write('\t'.join(l) + '\n')
        if site == 'Tokyo':
            g.write('\t'.join(l) + '\n')
        elif site == 'London':
            h.write('\t'.join(l) + '\n')
        else:
            pass


# 提取所有id到一个文件，检查文件中是否有重复id，有重复id说明数据还可以，因为每一条数据的单位不是照片而是每一个可以检测出emotion的face。（之前的曼哈顿因为程序的错误，每张照片只有一个emotion结果，所以此处应考虑改进）

# In[ ]:


with open('TokyoAndLondon1.txt') as f, open('All_id.txt', 'w', encoding='utf-8') as g:
    for line in f:
        pid = line.split('\t')[0]
        try:
            int(pid)
            g.write(pid + '\n')
        except:
            pass


#  统计总照片个数与情绪个数（都有地理坐标）

# In[ ]:


with open('All_id.txt') as f:
    s = set()
    count = 0
    for line in f:
        line = int(line.strip())
        s.add(line)
        count += 1
    print("照片数：{}".format(len(s)))
    print("情绪数：{}".format(count))


# 提取八个情绪值，用于主成份分析时直接粘贴进变量表

# In[ ]:


with open('Tokyo.txt') as f, open('Tokyo_for_pca.txt', 'w', encoding='utf-8') as g:
    count = 0
    for line in f:
        count += 1
        if count == 1:
            continue
        l = line.split('\t')
        l = [i.strip() for i in l]
        data = l[1:-2]
        g.write('\t'.join(data) + '\n')


# In[ ]:


with open('London.txt') as f, open('London_for_pca.txt', 'w', encoding='utf-8') as g:
    count = 0
    for line in f:
        count += 1
        if count == 1:
            continue
        l = line.split('\t')
        l = [i.strip() for i in l]
        data = l[1:-2]
        g.write('\t'.join(data) + '\n')

