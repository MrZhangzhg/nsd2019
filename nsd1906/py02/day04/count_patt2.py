import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        result = {}  # 保存结果
        cpatt = re.compile(patt)  # 编译模式，提升效率

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到了
                    key = m.group()
                    result[key] = result.get(key, 0) + 1

        return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.6789.1.232, 10.123.45.8
    br = 'Firefox|MSIE|Chrome'
    cp1 = CountPatt(fname)
    result1 = cp1.count_patt(ip)
    result2 = cp1.count_patt(br)
    print(result1)
    print(result2)
    print('*'* 30)

    cp2 = CountPatt('/etc/passwd')
    result3 = cp2.count_patt('nologin$|bash$')
    print(result3)
