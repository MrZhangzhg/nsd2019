import os
import subprocess

def ping(host):


if __name__ == '__main__':
    ips = ('172.40.63.%s' % i for i in range(1, 255))
    for ip in ips:
        ping(ip)
