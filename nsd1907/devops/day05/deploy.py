import os
import requests
import wget
import hashlib


def has_new_ver(ver_url, ver_fname):
    "有新版本返回True，没有返回False"
    # 本地没有版本文件，则有新版本
    if not os.path.exists(ver_fname):
        return True

    # 取出本地版本号
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    # 比较网上版本号和本地版本号，如果相同是没有新版本，否则有
    r = requests.get(ver_url)
    if local_ver == r.text:
        return False
    else:
        return True

def file_ok(fname, url):
    "如果网上md5值和本地文件计算出的md5值相同，返回True；否则返回False"
    # 计算本地文件的md5值
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 取出网上md5值，和本地计算的值进行比较
    r = requests.get(url)
    if m.hexdigest() == r.text.strip():
        return True
    else:
        return False


if __name__ == '__main__':
    # 判断是否有新版本，没有新版本退出
    ver_url = 'http://192.168.4.6/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本。')
        exit(1)

    # 下载新版本文件
    r = requests.get(ver_url)
    ver_num = r.text.strip()  # 去掉结尾的\n
    down_dir = '/var/www/download'
    app_url = 'http://192.168.4.6/deploy/pkgs/mysite-%s.tar.gz' % ver_num
    wget.download(app_url, down_dir)

    # 校验文件是否损坏，如果文件已损坏，则删除损坏文件并退出
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(down_dir, app_fname)
    md5_url = app_url + '.md5'
    if not file_ok(app_fname, md5_url):
        os.remove(app_fname)
        print('文件已损坏')
        exit(2)

    # 部署新版本

    # 更新本地版本
