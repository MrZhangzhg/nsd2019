import getpass
from email.mime.text import MIMEText
from email.header import Header
import smtplib

def send_mail(text, sender, recievers, subject, server, passwd):
    # 准备邮件正文，plain表示纯文本，富文本可以指定不同的格式
    msg = MIMEText(text, 'plain', 'utf8')
    # 配置邮件头部消息
    msg['From'] = Header(sender, 'utf8')
    msg['To'] = Header(recievers[0], 'utf8')
    msg['Subject'] = Header(subject, 'utf8')

    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(server)
    smtp.login(sender, passwd)
    # smtp.starttls()  # 如果服务器要求安全连接，打开此注释
    smtp.sendmail(sender, recievers, msg.as_bytes())

if __name__ == '__main__':
    text = 'python发送邮件测试\n'
    sender = 'zhangzhigang79@qq.com'
    recievers = ['zhangzhigang79@qq.com', 'zhangzhigang79@126.com']
    subject = 'py邮件测试'
    server = 'smtp.qq.com'
    passwd = getpass.getpass()  # 填写授权码，不是登陆密码
    send_mail(text, sender, recievers, subject, server, passwd)
