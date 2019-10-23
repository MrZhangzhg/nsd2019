

def has_new_ver():
    '用于判断是否有新版本，有新版本返回True'


def check_app():
    '用于校验软件包是否完好，完好返回True'


def deploy():


if __name__ == '__main__':
    # 没有新版本软件，则退出
    if not has_new_ver():
        print('未发现新版本。')
        exit(1)

    # 下载新版本软件包

    # 校验软件包是否完好，软件包已损坏的话，删除损坏的包，退出
    if not check_app():
        print('文件已损坏。')
        exit(2)

    # 部署软件包
    deploy()

    # 更新本地软件版本文件

