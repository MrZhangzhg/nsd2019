from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

# 准备邮件
message = MIMEText('Python email test\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')
message['To'] = Header('bob', 'utf8')
message['Subject'] = Header('py email', 'utf8')

# 发送邮件
smtp = SMTP('127.0.0.1')
smtp.sendmail('root', ['root', 'bob'], message.as_bytes())
