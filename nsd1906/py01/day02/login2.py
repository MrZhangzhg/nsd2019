import getpass   # 导入getpass模块

uname = input('用户名：')
upass = getpass.getpass('密码：')

if uname == 'bob' and upass == '123456':
    # 32是绿色，前景色，40以上是背景色
    # \033[0m是关闭颜色
    print('\033[32;1m登陆成功\033[0m')
else:
    print('\033[31;1m登陆失败\033[0m')


