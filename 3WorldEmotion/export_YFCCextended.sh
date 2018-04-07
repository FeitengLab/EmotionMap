#! /bin/sh
## 0 此脚本应该在 /mnt/tmp 目录运行（该目录容量较大，且已经修改权限，普通用户也可读写）
#    此脚本应该用 postgres 用户来运行，其他用户没有 psql 这个程序
# 如果不在，运行:
# cd /mnt/tmp
##
## 1. 导出 zip 文件
# SQL 语句写法及技巧见:
# [列出某个所有字段（仅字段）]https://github.com/FeitengLab/EmotionMap/blob/master/NotesForPostgreSQL.md#%E5%88%97%E5%87%BA%E6%9F%90%E4%B8%AA%E6%89%80%E6%9C%89%E5%AD%97%E6%AE%B5%E4%BB%85%E5%AD%97%E6%AE%B5
# [将指定表导出至压缩文件]https://github.com/FeitengLab/EmotionMap/blob/master/NotesForPostgreSQL.md#%E5%B0%86%E6%8C%87%E5%AE%9A%E8%A1%A8%E5%AF%BC%E5%87%BA%E8%87%B3%E5%8E%8B%E7%BC%A9%E6%96%87%E4%BB%B6
psql -c "copy (select id, userid, photo_date_taken, photo_date_uploaded, title, description, user_tags, longitude, latitude, accuracy, download_url, facenum, happiness, neutral, sadness, disgust, anger, fear, surprise, facequality_s, facequality_v, smile_s, smile_v, gender, ethnicity, age, country, smile_e from face) to STDOUT with delimiter E'\t' csv header" Face | zip > YFCCextended.zip
##

## 2. 修改文件名（默认文件名为`-`， 此处我们使用 zipnote 来修改(Ref: https://www.computerhope.com/unix/zipnote.htm)
#####################################
zipnote YFCCextended.zip > zip.tmp          # 导出 zip 文件内信息到 zip.tmp 文件
sed -i '2i@=YFCCextended.csv' zip.tmp       # 在 zip.tmp 第二行插入文本`@=YFCCextended.csv` ，即将文件名修改为这个YFCCextended.csv(Ref: https://stackoverflow.com/questions/6537490/insert-a-line-at-specific-line-number-with-sed-or-awk)
zipnote -w YFCCextended.zip < zip.tmp       # 将 修改后的 zip.tmp 写回 zip文件
rm zip.tmp                                  # 删除 zip.tmp 文件
#####################################

## 3. 其他处理
chmod 777 YFCCextended.zip # 修改权限，让大家都能访问
python3 send_mail.py       # 调用 python 脚本，给你发个邮件，告诉你自己任务完成啦
                           # 注意，这个脚本你不能直接使用，我已经将其隐私信息修改，你需要填写自己的，具体见脚本