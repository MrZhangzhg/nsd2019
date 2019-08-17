import os
import requests

def has_new_ver(ver_url, ver_fname):
    "有新版本返回True，否则返回False"
    # 本地没有版本文件，返回True
    if not os.path.exists(ver_fname):
        return True

    # 取出本地版本文件内容
    with open(ver_fname) as fobj:
        version = fobj.read()

    # 取出远程最新版本号
    r = requests.get(ver_url)

    # 判断版本号一致为False，不一致为True
    if version == r.text:
        return False
    else:
        return True

def check_app():
    "校验软件包，未损坏返回True，损坏返回False"

def deploy():
    "部署软件：解压、创建链接"

if __name__ == '__main__':
    # 如果未发现新版本，则退出
    dep_dir = '/var/www/deploy'
    ver_url = 'http://192.168.4.7/deploy/live_ver'
    ver_fname = os.path.join(dep_dir, 'live_ver')
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本。')
        exit(1)

    # 下载

    # 检查软件是否损坏，损坏则删除软件包并退出
    if not check_app():
        print('文件已损坏。')
        exit(2)

    # 部署
    deploy()

    # 更新本地live_ver文件
