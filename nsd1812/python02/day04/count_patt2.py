import re
from collections import Counter

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        cpatt = re.compile(patt)
        c = Counter()

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    c.update([m.group()])

        return c

if __name__ == '__main__':
    ip = '^(\d+\.){3}\d+'
    cp = CountPatt('access_log')
    result = cp.count_patt(ip)
    print(result)
    print(result.most_common(5))

    cp2 = CountPatt('/etc/passwd')
    shell = 'bash$|nologin$'
    print(cp2.count_patt(shell))
