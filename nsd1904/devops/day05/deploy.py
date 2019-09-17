"""自动发布web版本

1. 下载最新版本的软件
2. 检查下载的文件是否完好
3. 如果是完好的包，部署
"""

import os
import wget
import requests

def has_new_ver(ver_fname, ver_url):
    "如果本地没有版本文件，或版本低都返回True"
    if not os.path.exists(ver_fname):
        return True

    # 读取本地版本
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    # 本地版本和网上版本进行比较
    r = requests.get(ver_url)
    if local_ver != r.text:
        return True
    else:
        return False


def check_file(app_fname, md5_url):


def deploy(app_fname):


if __name__ == '__main__':
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.4.6/deploy/live_ver'
    # 如果没有新版本的软件，则退出
    if not has_new_ver(ver_fname, ver_url):
        print('未发现新版本软件。')
        exit(1)

    # 如果有新版本软件，则下载



    # 如果下载的软件已损坏，则把它删除，并退出
    app_fname = ''
    md5_url = ''
    if not check_file(app_fname, md5_url):
        print('文件已损坏。')
        exit(2)

    # 部署软件
    deploy(app_fname)

    # 更新最新版本信息
