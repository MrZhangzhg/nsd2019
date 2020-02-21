import subprocess
import threading

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        result = subprocess.run('ping -c2 %s &> /dev/null' % self.host, shell=True)
        if result.returncode == 0:
            print('%s:up' % self.host)
        else:
            print('%s:down' % self.host)

if __name__ == '__main__':
    ips = ['192.168.113.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=Ping(ip))  # target是Ping的实例
        t.start()  # 启动工作线程，执行target()  # 实例调用，将会执行__call__方法中的代码
