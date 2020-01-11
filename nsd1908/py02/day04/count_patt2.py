import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        patt_dict = {}
        cpatt = re.compile(patt)  # 为了更好的性能，将模式编译

        # 在文件的每一行进行模式匹配
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到了内容
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.67890.1.23  192.16.1.20
    cp = CountPatt(fname)
    result1 = cp.count_patt(ip)
    print(result1)
    br = 'Firefox|MSIE|Chrome'
    result2 = cp.count_patt(br)
    print(result2)
