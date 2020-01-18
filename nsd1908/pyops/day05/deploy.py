
def has_new_ver():
    '有新版本返回True，否则返回False'

def check_file():
    '如果文件md5值与网上提供的值一致，返回True; 否则返回False'

def deploy():
    '用于部署软件包'

if __name__ == '__main__':
    # 判断是否有新版本，没有则退出
    if not has_new_ver():
        print('没有发现新版本')
        exit(1)

    # 下载软件包

    # 校验软件包是否损坏，如损坏则删除它并退出
    if not check_file():
        print('文件已损坏')

        exit(2)

    # 部署软件包
    deploy()

    # 更新本地版本文件
