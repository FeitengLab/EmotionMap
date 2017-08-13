# encoding=utf-8

# 本脚本对本目录下的txt文件进行简单批量重命名
# 请首先确定已经将全部的压缩文件解压完毕，程序只需运行一次，请慎重操作

from glob import glob
from os import rename
for index, fname in enumerate(glob("*.txt")):
	new_name = "{}.csv".format(index)
	rename(fname, new_name)
	print("{!r} renamed to {!r}".format(fname, new_name))

input("Input any key to exit the program")