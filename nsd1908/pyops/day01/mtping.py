import threading
import subprocess

def ping(host):
    'ping通打印up，不通打印down'
    result = subprocess.run(
        'ping -c2 %s &> /dev/null' % host, shell=True
    )
    if result.returncode == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    ips = ['172.40.56.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=ping, args=(ip,))  # 创建线程
        t.start()  # 启动线程，target(*args)
