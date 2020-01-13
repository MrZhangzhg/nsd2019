import threading
import subprocess

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        'ping通打印up，不通打印down'
        result = subprocess.run(
            'ping -c2 %s &> /dev/null' % self.host, shell=True
        )
        if result.returncode == 0:
            print('%s:up' % self.host)
        else:
            print('%s:down' % self.host)

if __name__ == '__main__':
    ips = ['172.40.56.%s' % i for i in range(1, 255)]
    # target = Ping('172.40.56.1')
    # target()
    for ip in ips:
        t = threading.Thread(target=Ping(ip))  # 创建线程
        t.start()  # 启动线程，target(*args)
