import os
import requests
import wget
import hashlib
import tarfile

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

def check_file(app_fname, md5_url):
    '如果文件md5值与网上提供的值一致，返回True; 否则返回False'
    # 计算本地文件的md5值
    m = hashlib.md5()
    with open(app_fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 取出网上的md5值
    r = requests.get(md5_url)

    # 比较，注意，网上的md5值文件，要去除结尾的\n
    if m.hexdigest() == r.text.strip():
        return True
    else:
        return False

def deploy(app_fname, deploy_dir, dest):
    '用于部署软件包'
    # 解压缩
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 拼接出解压目录的绝对路径
    pkg_path = os.path.basename(app_fname)
    pkg_path = pkg_path.replace('.tar.gz', '')
    pkg_path = os.path.join(deploy_dir, pkg_path)

    # 如果软链接文件已经存在了，先删除它
    if os.path.exists(dest):
        os.remove(dest)

    # 创建软链接
    os.symlink(pkg_path, dest)


if __name__ == '__main__':
    # 判断是否有新版本，没有则退出
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.4.6/deploy/live_ver'
    if not has_new_ver(ver_fname, ver_url):
        print('没有发现新版本')
        exit(1)

    # 下载软件包
    down_dir = '/var/www/download'
    r = requests.get(ver_url)
    app_url = 'http://192.168.4.6/deploy/pkgs/myweb-%s.tar.gz' % r.text
    wget.download(app_url, down_dir)

    # 校验软件包是否损坏，如损坏则删除它并退出
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(down_dir, app_fname)
    md5_url = app_url + '.md5'
    if not check_file(app_fname, md5_url):
        print('文件已损坏')
        os.remove(app_fname)
        exit(2)

    # 部署软件包
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/nsd1908'
    deploy(app_fname, deploy_dir, dest)

    # 更新本地版本文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
