"""自动发布web版本

1. 下载最新版本的软件
2. 检查下载的文件是否完好
3. 如果是完好的包，部署
"""

import os
import wget
import requests
import hashlib
import tarfile

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
    "本地文件的值和网上提供的值一致，返回True；否则返回False"
    # 计算本地文件的md5值
    m = hashlib.md5()

    with open(app_fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 取出网上的md5值
    r = requests.get(md5_url)

    # 比较
    if m.hexdigest() == r.text.strip():
        return True
    else:
        return False


def deploy(app_fname):
    "将压缩包解压到deploy_dir目录，并为其创建链接"
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd1904'

    # 解压
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 取出解压后文件的绝对路径
    fname = app_fname.split('/')[-1]
    app_dir = fname.replace('.tar.gz', '')
    app_dir = os.path.join(deploy_dir, app_dir)

    # 如果链接文件已经存在，需要将它删除
    if os.path.exists(dest):
        os.remove(dest)

    # 创建链接
    os.symlink(app_dir, dest)


if __name__ == '__main__':
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.4.6/deploy/live_ver'
    # 如果没有新版本的软件，则退出
    if not has_new_ver(ver_fname, ver_url):
        print('未发现新版本软件。')
        exit(1)

    # 如果有新版本软件，则下载
    download_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = 'http://192.168.4.6/deploy/pkgs/mysite-%s.tar.gz' % r.text
    wget.download(app_url, download_dir)

    # 如果下载的软件已损坏，则把它删除，并退出
    app_fname = app_url.split('/')[-1]  # 取出压缩包名
    app_fname = os.path.join(download_dir, app_fname)  # 拼接绝对路径
    md5_url = app_url + '.md5'
    if not check_file(app_fname, md5_url):
        print('文件已损坏。')
        os.remove(app_fname)
        exit(2)

    # 部署软件
    deploy(app_fname)

    # 更新最新版本信息
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
