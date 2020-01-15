from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件正文，plain表示纯文本，富文本可以指定不同的格式
msg = MIMEText('This is a python email test.\n', 'plain', 'utf8')
# 配置邮件头部消息
msg['From'] = Header('root', 'utf8')
msg['To'] = Header('tom', 'utf8')
msg['Subject'] = Header('py test', 'utf8')

# 发送邮件
smtp = smtplib.SMTP('127.0.0.1')
smtp.sendmail('root', ['tom', 'root'], msg.as_bytes())
