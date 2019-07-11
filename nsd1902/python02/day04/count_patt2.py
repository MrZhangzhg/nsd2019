'用于统计一个文件中某些字段出现的次数'
import re


class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        patt_dict = {}
        cpatt = re.compile(patt)

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    key = m.group()   # 取出模式
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    logfile = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 192.168.1.10   1234.56789.10.123456
    cp = CountPatt(logfile)
    print(cp.count_patt(ip))

    userfile = '/etc/passwd'
    shell = 'bash$|nologin$'
    cp2 = CountPatt(userfile)
    print(cp2.count_patt(shell))
