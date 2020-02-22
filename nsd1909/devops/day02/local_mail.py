from email.mime.text import MIMEText
from email.header import Header
import smtplib

# 准备邮件
# plain表示纯文本，相对于富文本
msg = MIMEText('python 邮件测试\n', 'plain', 'utf8')
# 添加头部消息
msg['From'] = Header('root', 'utf8')  # 发件人
msg['To'] = Header('tom', 'utf8')     # 收件人
msg['Subject'] = Header('py test', 'utf8')   # 主题

# 发送邮件
smtp = smtplib.SMTP('localhost')      # 使用本机发送邮件
smtp.sendmail('root', ['tom', 'jerry'], msg.as_bytes())
