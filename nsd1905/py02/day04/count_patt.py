import re

def count_patt(fname, patt):
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
    ip = '^(\d+\.){3}\d+'  # 1234.56789.10.8  1.23.123.5
    br = 'Firefox|MSIE|Chrome'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
    result3 = list(result1.items())
    result3.sort(key=lambda seq: seq[-1], reverse=True)
    print(result3)
