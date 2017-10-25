import subprocess

from os.path import splitext

def unzip_rename(zipfile):
    # 解压文件并重命名
    newfile = splitext(zipfile)[0] + '.txt'
    subprocess.call('unzip {}'.format(zipfile), shell=True)
    subprocess.call('mv - {}'.format(newfile))
    return newfile