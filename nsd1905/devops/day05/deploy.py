import os
import requests
import wget
import hashlib
import tarfile


def has_new_ver(ver_fname, ver_url):
    '用于判断是否有新版本，有新版本返回True'
    # 如果本地没有版本文件，则有新版本；本地和远程版本不一样，有新版本
    if not os.path.isfile(ver_fname):
        return True

    # 取出远程版本号
    r = requests.get(ver_url)

    # 远程版本与本地版本比较
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    if local_ver != r.text:
        return True
    else:
        return False


def check_app(app_fname, md5_url):
    '用于校验软件包是否完好，完好返回True'
    # 计算文件的md5值
    m = hashlib.md5()
    with open(app_fname, 'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    # 在网上取出公布的md5值
    r = requests.get(md5_url)

    # 判断两个值是否相等
    if m.hexdigest() == r.text.strip():
        return True
    else:
        return False

def deploy(app_fname, deploy_dir):
    '部署软件包到web服务器'
    # 解压到部署目录
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 拼接出解压目录的绝对路径
    dest = app_fname.split('/')[-1]
    dest = dest.replace('.tar.gz', '')
    dest = os.path.join(deploy_dir, dest)

    # 创建链接
    link = '/var/www/html/nsd1905'
    if os.path.exists(link):  # 如果链接文件已存在，先删除它
        os.remove(link)
    os.symlink(dest, link)


if __name__ == '__main__':
    # 没有新版本软件，则退出
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.4.6/deploy/live_ver'
    if not has_new_ver(ver_fname, ver_url):
        print('未发现新版本。')
        exit(1)

    # 下载新版本软件包
    r = requests.get(ver_url)
    ver = r.text.strip()  # 去除文件结尾的\n
    app_url = 'http://192.168.4.6/deploy/pkgs/website-%s.tar.gz' % ver
    download_dir = '/var/www/download'
    wget.download(app_url, download_dir)

    # 校验软件包是否完好，软件包已损坏的话，删除损坏的包，退出
    md5_url = app_url + '.md5'
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    if not check_app(app_fname, md5_url):
        os.remove(app_fname)
        print('文件已损坏。')
        exit(2)

    # 部署软件包
    deploy_dir = '/var/www/deploy'
    deploy(app_fname, deploy_dir)

    # 更新本地软件版本文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
