import re

class CountPatt:
    def count_patt(self, fname, patt):
        result = {}
        cpatt = re.compile(patt)

        with open(fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    key = m.group()
                    result[key] = result.get(key, 0) + 1

        return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    cp = CountPatt()
    ip_dict = cp.count_patt(fname, ip)
    print(ip_dict)
