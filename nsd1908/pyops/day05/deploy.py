import os
import requests

def has_new_ver(ver_fname, ver_url):
    '有新版本返回True，否则返回False'
    # 本地没有版本文件，返回True
    if not os.path.isfile(ver_fname):
        return True

    # 如果本地版本和网上版本不一样，则返回True
    with open(ver_fname) as fobj:
        local_ver = fobj.read()
    r = requests.get(ver_url)
    if local_ver != r.text:
        return True
    else:
        return False

def check_file():
    '如果文件md5值与网上提供的值一致，返回True; 否则返回False'

def deploy():
    '用于部署软件包'

if __name__ == '__main__':
    # 判断是否有新版本，没有则退出
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.4.6/deploy/live_ver'
    if not has_new_ver(ver_fname, ver_url):
        print('没有发现新版本')
        exit(1)

    # 下载软件包

    # 校验软件包是否损坏，如损坏则删除它并退出
    if not check_file():
        print('文件已损坏')

        exit(2)

    # 部署软件包
    deploy()

    # 更新本地版本文件
