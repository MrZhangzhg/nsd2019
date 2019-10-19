from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件
msg = MIMEText('python邮件测试\n', 'plain', 'utf8')  # 邮件正文
msg['From'] = Header('root', 'utf8')  # 发件人
msg['To'] = Header('bob', 'utf8')     # 收件人
msg['Subject'] = Header('py test')    # 主题

# 发送邮件
smtp = smtplib.SMTP('localhost')  # 将本机作为邮件服务器
# 指定发件人、收件人列表、发送的消息
smtp.sendmail('root', ['root', 'bob'], msg.as_bytes())
