import requests
import wget
import os

def has_new_ver(ver_url, ver_fname):


def check_pkgs(md5_url, pkg_path):


def deploy(pkg_path, deploy_dir):


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
    deploy(pkg_path, deploy_dir)
    with open(ver_fname, 'w') as fobj:
        fobj.write(r.text)
