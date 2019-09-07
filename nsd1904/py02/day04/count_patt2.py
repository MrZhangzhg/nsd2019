import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        cpatt = re.compile(patt)  # 为了效率，先编译模式
        result = {}  # 用于保存结果

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到，匹配对象表示真；没匹配到，返回None，表示假
                    key = m.group()  # 取出匹配内容
                    result[key] = result.get(key, 0) + 1

        return result


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 192.168.1.15   1234.56789.1.12345678
    br = 'Firefox|MSIE|Chrome'
    os_patt = 'Linux|Windows|Android'
    cp = CountPatt(fname)
    print(cp.count_patt(ip))
    print(cp.count_patt(br))
    print(cp.count_patt(os_patt))
    print('#' * 50)
    cp1 = CountPatt('/etc/passwd')
    print(cp1.count_patt('bash$|nologin$'))
