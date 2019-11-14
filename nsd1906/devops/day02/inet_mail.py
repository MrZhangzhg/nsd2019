from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_mail(body, sender, receivers, subject, host, passwd):
    # 准备邮件
    msg = MIMEText(body, 'plain', 'utf8')
    msg['From'] = Header(sender, 'utf8')
    msg['To'] = Header(receivers[0], 'utf8')
    msg['Subject'] = Header(subject, 'utf8')

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(host)
    # smtp.starttls()  # 如果服务器要求安全通信，打开此注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, msg.as_bytes())
    smtp.close()

if __name__ == '__main__':
    body = '这是一封来自python的邮件测试\n'
    sender = 'zhangzhigang79@126.com'
    receivers = ['zhangzhigang79@126.com']
    subject = 'py test'
    host = 'smtp.126.com'
    passwd = getpass.getpass()
    send_mail(body, sender, receivers, subject, host, passwd)
