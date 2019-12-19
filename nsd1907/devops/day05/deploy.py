import os
import requests
import wget
import hashlib
import tarfile


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

def deploy(app_fname, deploy_dir, dest):
    # 将压缩包解压至deploy_dir
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 拼接出解压目录的绝对路径
    app_path = os.path.basename(app_fname)
    app_path = app_path.replace('.tar.gz', '')
    app_path = os.path.join(deploy_dir, app_path)

    # 如果目标软链接已存在，先删除它
    if os.path.exists(dest):
        os.remove(dest)

    # 创建软链接
    os.symlink(app_path, dest)


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
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd1907'
    deploy(app_fname, deploy_dir, dest)

    # 更新本地版本
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
