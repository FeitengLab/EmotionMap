import subprocess

# 服务器端运行，postgres home目录nohup运行

# 将文件导出为zip文件
out = "psql -c \"copy public.{0} to stdout with delimiter E'\t' csv header\"  Flickr1 | zip > /tmp/{0}.zip"
# 计算文件按checksum
sha1 = "sha1sum /tmp/{0}.zip > /tmp/{0}.zip.sha1"
name = 'flickr{}'

for i in range(0, 5): # 按照剩余存储空间，来决定数量
    print("running for {}".format(name.format(i)))
    print("Output table to zip")
    subprocess.call(out.format(name.format(i)), shell=True)
    print("checksum the zip")
    subprocess.call(sha1.format(name.format(i)), shell=True)
