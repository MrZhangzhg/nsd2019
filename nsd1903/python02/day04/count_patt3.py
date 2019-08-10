import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        result = {}
        cpatt = re.compile(patt)

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    key = m.group()
                    result[key] = result.get(key, 0) + 1

        return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'MSIE|Firefox|Chrome'
    cp = CountPatt(fname)
    ip_dict = cp.count_patt(ip)
    print(cp.count_patt(br))
    print(ip_dict)

    cp2 = CountPatt('/etc/passwd')
    print(cp2.count_patt('bash$|nologin$'))
