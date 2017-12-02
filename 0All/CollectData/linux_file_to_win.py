import subprocess
import os

from unzip_rename import unzip_rename

# 此处需要填写服务器IP，端口，用户名和密码，因上传github，此处隐去这些隐私信息
ip = "xx.xx.xx.xx"
user = "xx"
port = 22
passwd = 'xx'

def download(linux_path, method='.sha1'):
    win_path = os.path.basename(linux_path)
    # 下载服务器目标文件
    print('Downloading file: ')
    child1 = subprocess.call("{} -P {} -pw {} {}@{}:{} {}".format('pscp',
                                                                  port, passwd,
                                                                  user, ip,
                                                                  linux_path,
                                                                  win_path), shell=True)

    # 下载服务器checksum文件
    print('Downloading checksum file: ')
    child2 = subprocess.call("{} -P {} -pw {} {}@{}:{} {}".format('pscp',
                                                                  port, passwd,
                                                                  user, ip,
                                                                  linux_path+method,
                                                                  win_path+method), shell=True)
    
    return win_path
def sha1(win_path):
    """sha1sum results of one file"""
    return subprocess.check_output('sha1sum {}'.format(win_path), shell="True").decode()

def compare_sum(win_path, method='.sha1'):
    """比较本地文件和远程服务器文件checksum"""
    local = sha1(win_path)[:40]
    with open(win_path+method) as f:
        remote = f.read()[:40]
    print('local file checksum :\n{!r}'.format(local))
    print('remote file checksum :\n{!r}'.format(remote))
    if local == remote:
        print("File integrity is perfect")
        return True
    else:
        print('Warning: integrity of file {!r} seems not good ! Please check manually !'.format(win_path))
        return False

def download_check(linux_path):
    # 下载一个文件并检查文件完整性
    print('Download task begins: ')
    win_path = download(linux_path) # 注意此处为相对路径，也就是只有文件名
    print('Download complete!')
    print('Calculate local file checksum')
    compare_sum(win_path)
    print('Task ended!')
    return win_path

if __name__ == "__main__":
    path_temp = '/tmp/flickr{}.zip'
    unzip_flag = False
    for i in [5, 22, 25]:
        path = path_temp.format(i)
        win_path = download_check(path)
        if unzip_flag:
            unzip_rename(win_path)