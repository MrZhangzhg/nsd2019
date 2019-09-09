import subprocess
import threading

class Ping:
    def __call__(self, host):
        result = subprocess.run(
            'ping -c2 %s &> /dev/null' % host,
            shell=True
        )
        if result.returncode == 0:
            print('%s:up' % host)
        else:
            print('%s:down' % host)

if __name__ == '__main__':
    ips = ('172.40.59.%s' % i for i in range(1, 255))
    for ip in ips:
        t = threading.Thread(target=Ping(), args=(ip,))  # 创建实例
        t.start()  # target(*args)  # 调用实例
