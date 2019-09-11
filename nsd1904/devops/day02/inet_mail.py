from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def inet_mail(host, sender, passwd, receivers, subject, body):
    # 准备邮件正文，plain表示纯文本
    message = MIMEText(body, 'plain', 'utf8')
    message['From'] = Header(sender, 'utf8')  # 发件人
    message['To'] = Header(receivers[0], 'utf8')  # 收件人
    message['Subject'] = Header(subject, 'utf8')  # 主题

    # 发邮件
    smtp = smtplib.SMTP()
    smtp.connect(host)
    # smtp.starttls()   # 如果服务器要求安全连接，则打开注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, message.as_bytes())

if __name__ == '__main__':
    passwd = getpass.getpass()
    server = 'smtp.126.com'
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    subject = 'py inet邮件测试'
    body = "你好，这是一个测试，不用回复\r\n"
    inet_mail(server, sender, passwd, receivers, subject, body)
