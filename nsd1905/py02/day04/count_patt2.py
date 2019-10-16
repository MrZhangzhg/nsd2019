import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        patt_dict = {}
        cpatt = re.compile(patt)  # 编译模式，提升效率

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到，则为真，匹配不到是None，为假
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Firefox|MSIE|Chrome'
    cp = CountPatt(fname)
    result1 = cp.count_patt(ip)
    result2 = cp.count_patt(br)
    print(result1)
    print(result2)
