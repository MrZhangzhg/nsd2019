from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件
msg = MIMEText('这是一封Python邮件测试\n', 'plain', 'utf8')
msg['From'] = Header('root', 'utf8')
msg['To'] = Header('bob', 'utf8')
msg['Subject'] = Header('py test', 'utf8')

# 发送邮件
smtp = smtplib.SMTP('127.0.0.1')
smtp.sendmail('root', ['root', 'bob'], msg.as_bytes())
smtp.close()
