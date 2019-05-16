import re
from collections import Counter

def count_patt(fname, patt):
    cpatt = re.compile(patt)  # 先编译模式
    c = Counter()  # 用于保存结果

    # 打开文件，从每一行中匹配，将匹配结果更新到c中
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 如果匹配到内容，才是真；None是False
                c.update([m.group()])

    return c

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'   # 192.168.1.23, 12345.67890.1.132234354
    br = 'Firefox|MSIE|Chrome'
    ips = count_patt(fname, ip)
    print(ips)
    print(ips.most_common(5))
    print(count_patt(fname, br))
