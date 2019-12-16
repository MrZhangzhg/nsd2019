from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件
# 正文, 纯文本文件, 编码
message = MIMEText('My Python email text.\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')
message['To'] = Header('tom', 'utf8')
message['Subject'] = Header('email test', 'utf8')

# 发送邮件
smtp = smtplib.SMTP('localhost')
smtp.sendmail('root', ['root', 'tom'], message.as_string())
