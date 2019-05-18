from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP
import getpass

def send_email(server, passwd, sender, recievres, subject, message):
    msg = MIMEText(message, 'plain', 'utf8')
    msg['From'] = Header(sender, 'utf8')
    msg['To'] = Header(recievres[0], 'utf8')
    msg['Subject'] = Header(subject, 'utf8')

    smtp = SMTP(server)
    # smtp.starttls()   # 如果邮件服务器要求安全连接，打开此注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, recievres, msg.as_bytes())

if __name__ == '__main__':
    server = 'smtp.126.com'
    sender = 'zhangzhigang79@126.com'
    passwd = getpass.getpass()
    recievres = ['zhangzhigang79@126.com']
    subject = '126 mail test'
    message = 'Hello World!\n'
    send_email(server, passwd, sender, recievres, subject, message)
