from email.mime.text import MIMEText
from email.header import Header
import smtplib
import getpass

def send_email(body, sender, receivers, subject, server, passwd):
    # 准备邮件
    msg = MIMEText(body, 'plain', 'utf8')
    # 添加头部消息
    msg['From'] = Header(sender, 'utf8')  # 发件人
    msg['To'] = Header(receivers[0], 'utf8')     # 收件人
    msg['Subject'] = Header(subject, 'utf8')   # 主题

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(server)
    # smtp.starttls()   # 如果服务器要求安全连接，则打开此注释
    smtp.login(sender, passwd)
    smtp.sendmail(sender, receivers, msg.as_bytes())

if __name__ == '__main__':
    body = 'python发送邮件测试。\n'
    sender = 'zhangzhigang79@qq.com'
    receivers = ['zhangzhigang79@qq.com', 'zhangzhigang79@126.com']
    subject = 'py mail'
    server = 'smtp.qq.com'
    passwd = getpass.getpass()
    send_email(body, sender, receivers, subject, server, passwd)
