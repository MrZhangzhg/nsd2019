import re

class CountPatt:
    def count_patt(self, fname, patt):
        patt_dict = {}
        cpatt = re.compile(patt)  # 编译模式，提升效率

        with open(fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:  # 如果匹配到，则为真，匹配不到是None，为假
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1

        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    cp = CountPatt()
    result1 = cp.count_patt(fname, ip)
    print(result1)
