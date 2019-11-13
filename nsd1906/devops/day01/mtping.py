import subprocess
import threading

def ping(host):
    result = subprocess.run(
        'ping -c2 %s &> /dev/null' % host, shell=True
    )
    if result.returncode == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)


if __name__ == '__main__':
    ips = ('172.40.84.%s' % i for i in range(1, 255))
    for ip in ips:
        # 创建工作线程
        t = threading.Thread(target=ping, args=(ip,))
        # 启动工作线程，就是调用相应的函数，函数结束，工作线程也就结束了
        t.start()  # 调用target(*args)
