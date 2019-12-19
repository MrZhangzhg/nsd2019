

def has_new_ver(ver_url, ver_fname):
    "有新版本返回True，没有返回False"



if __name__ == '__main__':
    # 判断是否有新版本，没有新版本退出
    ver_url = 'http://192.168.4.6/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本。')
        exit(1)

    # 下载新版本文件

    # 校验文件是否损坏，如果文件已损坏，则删除损坏文件并退出

    # 部署新版本

    # 更新本地版本
