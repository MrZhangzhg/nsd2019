import requests
import wget
import os
import hashlib
import tarfile

def has_new_ver(ver_url, ver_fname):
    # 如果本地没有版本文件，则有新版本
    if not os.path.isfile(ver_fname):
        return True

    # 取出本地版本
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    # 如果本地版本和远程版本不一致，则有新版本
    r = requests.get(ver_url)
    if local_ver != r.text:
        return True

    return False

def check_pkgs(md5_url, pkg_path):
    # 取出远程md5值
    r = requests.get(md5_url)
    remote_md5 = r.text.strip()

    m = hashlib.md5()
    with open(pkg_path, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    local_md5 = m.hexdigest()

    if local_md5 == remote_md5:
        return True

    return False

def deploy(pkg_path, deploy_dir, version):
    dest = '/var/www/html/nsd1812'
    src = '/var/www/deploy/myweb-%s' % version
    tar = tarfile.open(pkg_path, 'r')
    tar.extractall(path=deploy_dir)
    tar.close()

    # 如果目标链接已存在，先删除，否则无法创建
    if os.path.exists(dest):
        os.remove(dest)

    # 创建链接
    os.symlink(src, dest)

if __name__ == '__main__':
    # 如果没有新版本则退出
    ver_url = 'http://192.168.122.73/deploy/livever'
    ver_fname = '/var/www/deploy/livever'
    download_dir = '/var/www/download/'
    deploy_dir = '/var/www/deploy/'
    if not has_new_ver(ver_url, ver_fname):
        print('没有发现新版本')
        exit(1)

    # 有新版本，下载软件压缩包
    r = requests.get(ver_url)
    version = r.text.strip()
    pkg_url = 'http://192.168.122.73/deploy/pkgs/myweb-%s.tar.gz' % version
    wget.download(pkg_url, download_dir)

    # 检查软件包是否损坏
    pkg_path = pkg_url.split('/')[-1]
    pkg_path = os.path.join(download_dir, pkg_path)
    md5_url = pkg_url + '.md5'
    if not check_pkgs(md5_url, pkg_path):
        print('软件包已损坏')
        os.remove(pkg_path)
        exit(2)

    # 如果软件压缩包是完好的，则部署，并更新软件版本文件
    deploy(pkg_path, deploy_dir, version)
    with open(ver_fname, 'w') as fobj:
        fobj.write(r.text)
