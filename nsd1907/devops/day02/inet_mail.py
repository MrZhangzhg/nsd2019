from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def inet_mail(text, sender, recievers, subject, server, passwd):
    # 准备邮件
    # 正文, 纯文本文件, 编码
    message = MIMEText(text, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(recievers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(server)
    # smtp.starttls()  # 如果服务器要求安全连接，打开此注释
    smtp.login(user=sender, password=passwd)
    smtp.sendmail(sender, recievers, message.as_string())

if __name__ == '__main__':
    text = 'py发送邮件测试\n'
    sender = 'zhangzhigang79@qq.com'
    recievers = ['zhangzhigang79@126.com']
    server = 'smtp.qq.com'
    subject = 'py test'
    pwd = getpass.getpass()
    inet_mail(text, sender, recievers, subject, server, pwd)
