from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_mail(msg, subject, sender, receivers, host, passwd):
    # 准备邮件
    message = MIMEText(msg, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')
    message['To'] = Header(receivers[0], 'utf8')
    message['Subject'] = Header(subject, 'utf8')

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(host)  # 连接服务器
    # smtp.starttls()  # 类似于https，如果需要安全连接，打开此注释
    smtp.login(sender, passwd)  # 登陆，密码填你的授权码
    smtp.sendmail(sender, receivers, message.as_bytes())
    smtp.close()  # 关闭连接

if __name__ == '__main__':
    msg = '互联网邮件测试\n'
    subject = 'py test'
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    host = 'smtp.126.com'
    passwd = getpass.getpass()
    send_mail(msg, subject, sender, receivers, host, passwd)
