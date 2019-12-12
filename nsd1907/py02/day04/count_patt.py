import re


def count_patt(fname, patt):
    cpatt = re.compile(patt)  # 为了更好的执行效率，把模式编译
    patt_dict = {}  # 把结果保存到字典

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)  # 在一行中匹配模式
            if m:  # 如果m不是None，非空为真
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1
                # if key not in patt_dict:
                #     patt_dict[key] = 1
                # else:
                #     patt_dict[key] += 1
    return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.67890.1.10  192.16.1.123
    br = 'Chrome|MSIE|Firefox'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
