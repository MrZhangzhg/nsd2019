from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件正文，plain表示纯文本
message = MIMEText('Python email test.\r\n', 'plain', 'utf8')
message['From'] = Header('root', 'utf8')  # 发件人
message['To'] = Header('tom', 'utf8')  # 收件人
message['Subject'] = Header('py test', 'utf8')  # 主题

# 发邮件
smtp = smtplib.SMTP()
smtp.connect('localhost')
smtp.sendmail('root', ['tom', 'bob'], message.as_bytes())


