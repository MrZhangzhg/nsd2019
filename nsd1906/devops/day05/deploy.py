import wget
import os
import requests
import hashlib

def has_new_ver(ver_url, ver_fname):
    '有新版本返回True，否则返回False'
    # 如果本地没有版本文件，则为True
    if not os.path.isfile(ver_fname):
        return True

    # 取出本地版本
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    # 本地版本与网上版本比较，如果不一致返回True
    r = requests.get(ver_url)
    if local_ver != r.text:
        return True
    else:
        return False


def file_ok(md5_url, fname):
    '如果文件已损坏返回False，否则返回True'
    # 计算本地文件的md5值
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 取出网上的md5值，进行比较
    r = requests.get(md5_url)
    if m.hexdigest() == r.text.strip():
        return True
    else:
        return False

def deploy():
    '部署软件'

if __name__ == '__main__':
    # 判断是否有新版本，没有则退出
    ver_url = 'http://192.168.4.6/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本。')
        exit(1)

    # 下载新版本软件
    r = requests.get(ver_url)
    ver = r.text.strip()  # 把额外的\n删除，得到版本
    app_url = 'http://192.168.4.6/deploy/pkgs/website-%s.tar.gz' % ver
    down_dir = '/var/www/download'
    wget.download(app_url, down_dir)

    # 校验。如果下载的文件已损坏，删除它
    md5_url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(down_dir, app_fname)
    if not file_ok(md5_url, app_fname):
        os.remove(app_fname)
        print('文件已损坏。')
        exit(2)

    # 部署软件
    deploy()

    # 更新live_ver文件的版本

