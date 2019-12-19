import os
import requests
import wget


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


    # 部署新版本

    # 更新本地版本
