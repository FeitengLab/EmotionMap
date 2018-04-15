# python3
# WJL
"""
使用 QQ邮箱给你的邮箱发送简单的邮件。

使用方法:
1. 首先先要按照下面的提示填写好你的邮箱发信地址授权码等配置

2. 将文件复制到你的工作路径，开始使用
使用方法一（直接运行）：
跳到最后一行，填上你喜欢的邮件主题，并在邮件内容中其中添加你需要的必要信息，比如程序运行时间，当前时间等
最后，命令行运行即可（也就是说你可以直接把这一行写到shell脚本）。
    python3 send_mail.py
使用方法二（间接）：
在其他脚本里 from send_mail import send_qq_mail，填上主题和内容即可。

3. 注意：
填了私人信息的脚本仅供自己使用，没有去除私人信息的不要分享!!!

主题一般一行，内容可以有多行，自己使用 \n 分行。
"""
import smtplib

from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

################################################################################
# 下面是你需要修改的配置
################################################################################
fromaddr = "xxxx@qq.com" # 发信地址，你的 QQ 邮箱
toaddrs = "xxxx@outlook.com" # 收信地址，你的其他邮箱，可以及时收到的（随便填，别人的也行）
username = "xxxx@qq.com" # 支持SMTP的账号，用于登录服务器，此处还是你的这个 QQ 邮箱
password = "xxxx" # 密码，可以填写QQ邮箱密码，但是不安全，应填写授权码。请看下面注释。
################################################################################
'''
授权码申请方法： 登录QQ邮箱网页端，点击上方“设置”进入邮箱设置，选择“账户”，
往下翻，找到开启服务， “POP3/SMTP服务 ”，点击后面的开启，下方温馨提示里点击生成授权码。
（需要发短信之类的验证你的身份）

提示： 上方密码不要使用自己的QQ密码或者QQ邮箱密码，使用授权码即可。 
如果你的代码需要上传到公开可获取的地方，一定要记得删除或者替换此授权码，我这个地方就是
这么处理的。
其他敏感信息也是如此，切记切记。
'''

def send_qq_mail(subject, body):
    '''
    Arguments:
    subject - 必填，邮件主题
    body - 必填，邮件内容

    '''
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = fromaddr
    msg["To"] = toaddrs
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()

if __name__ == "__main__":
    subject = 'Job is done, zip file is well prepared'
    content = 'Checkout it in the directory /mnt/tmp/YFCCextended.zip'
              '\n\nHappy day😊\n {time}'.format(time=datetime.now())
    send_qq_mail(subject, content)