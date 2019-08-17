
def has_new_ver():
    "有新版本返回True，否则返回False"

def check_app():
    "校验软件包，未损坏返回True，损坏返回False"

def deploy():
    "部署软件：解压、创建链接"

if __name__ == '__main__':
    # 如果未发现新版本，则退出
    if not has_new_ver():
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
