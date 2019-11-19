import wget

def has_new_ver(ver_url, ver_fname):
    '有新版本返回True，否则返回False'

def file_ok():
    '如果文件已损坏返回False，否则返回True'

def deploy():
    '部署软件'

if __name__ == '__main__':
    # 判断是否有新版本，没有则退出
    ver_url = 'http://192.168.4.6/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_url, ver_fname):
        print('未发现新版本。')
        exit(1)

    # 下载新版本软件
    app_url = 'http://192.168.4.6/deploy/pkgs/website-1.0.tar.gz'
    down_dir = '/var/www/download'
    wget.download(app_url, down_dir)

    # 校验。如果下载的文件已损坏，删除它
    if not file_ok():
        print('文件已损坏。')
        exit(2)

    # 部署软件
    deploy()

    # 更新live_ver文件的版本
    
