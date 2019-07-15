import getpass
from email.header import Header
from email.mime.text import MIMEText
import smtplib

def send_mail(host, password, sender, receivers, body, subject):
    # 邮件头部信息：发件人、收件人、主题
    msg = MIMEText(body, 'plain', 'utf8')
    msg['From'] = Header(sender, 'utf8')
    msg['To'] = Header(receivers[0], 'utf8')
    msg['Subject'] = Header(subject, 'utf8')

    # 发邮件：邮件服务器、发件人、收件人
    smtp = smtplib.SMTP()
    smtp.connect(host)
    # smtp.starttls()   # 如果服务器需要安全连接，打开此注释
    smtp.login(sender, password)  # 登陆
    smtp.sendmail(sender, receivers, msg.as_bytes())

if __name__ == '__main__':
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    server = 'smtp.126.com'
    password = getpass.getpass()
    body = 'Hello from python'
    subject = 'py mail test'
    send_mail(server, password, sender, receivers, body, subject)
