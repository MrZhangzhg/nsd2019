import os
import requests
import wget
import hashlib
import tarfile

def has_new_ver(ver_url, ver_fname):
    "用于检查是否有新版本，返回值是True/False"
    # 如果本地没有版本文件或本地版本文件与网上livever不一样，就是有新版本
    if not os.path.isfile(ver_fname):
        return True

    r = requests.get(ver_url)  # 网上版本号
    with open(ver_fname) as fobj:
        local_ver = fobj.read()   # 本地文件中的版本号

    if r.text != local_ver:   # 本地和网上的版本号不一样，有新版本
        return True

    return False


def check_app(app_fname, app_md5_url):
    "用于检查下载的压缩包是否未损坏，完好返回值是True/损坏返回值是False"
    # 计算出本地文件的md5值
    m = hashlib.md5()
    with open(app_fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    result = m.hexdigest()

    r = requests.get(app_md5_url)  # 取出网上的md5值
    if result == r.text.strip():   # 本地和网上的md5值相同，则未损坏
        return True

    return False


def deploy(app_fname, web_root):
    "用于部署应用"
    # 解压软件包到目标
    dest = '/var/www/deploy'
    tar = tarfile.open(app_fname)
    tar.extractall(path=dest)
    tar.close()

    # 拼接出解压目录的绝对路径
    app_dir = app_fname.split('/')[-1]
    app_dir = app_dir.replace('.tar.gz', '')
    app_dir = os.path.join(dest, app_dir)

    # 创建链接。如果链接已存在，先将其删除
    if os.path.exists(web_root):
        os.remove(web_root)

    os.symlink(app_dir, web_root)

if __name__ == '__main__':
    # 判断是否有新版本，没有的话退出
    ver_url = 'http://192.168.4.7/deploy/livever'
    ver_fname = '/var/www/deploy/livever'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本。')
        exit(1)

    # 下载软件
    r = requests.get(ver_url)
    version = r.text.strip()
    app_url = 'http://192.168.4.7/deploy/packages/myweb-%s.tar.gz' % version
    download_dir = '/var/www/download'
    wget.download(app_url, download_dir)

    # 检查压缩包是否损坏
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    app_md5_url = app_url + '.md5'
    if not check_app(app_fname, app_md5_url):
        print('压缩包已损坏')
        os.remove(app_fname)  # 删除损坏的压缩包
        exit(2)

    # 更新本地版本文件
    with open(ver_fname, 'w') as fobj:
        fobj.write(version + '\n')

    # 部署软件包
    web_root = '/var/www/html/nsd1902'
    deploy(app_fname, web_root)
