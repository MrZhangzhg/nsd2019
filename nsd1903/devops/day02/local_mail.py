from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件, 纯文本文件
message = MIMEText('python email测试\r\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')
message['To'] = Header('bob', 'utf8')
message['Subject'] = Header('py email test')

# 发送邮件
smtp = smtplib.SMTP('127.0.0.1')
smtp.sendmail('root', ['root', 'bob'], message.as_bytes())

# 查看本地邮件 mail
# 查看指定用户的邮件 mail -u 用户
