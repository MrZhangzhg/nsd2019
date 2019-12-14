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
    ips = ['172.40.52.%s' % i for i in range(1, 255)]
    for ip in ips:
        # 创建Thread的实例，target接受一个函数作为参数
        # args是一个序列对象，保存函数的参数
        t = threading.Thread(target=ping, args=(ip,))
        # 启动线程，即执行target(*args)
        t.start()
