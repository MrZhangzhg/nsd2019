
def count_patt(fname, patt):
    '用于在文件中统计每个模式字符串出现的次数'


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1234.56789.10.2  192.168.10.5
    br = 'Firefox|MSIE'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
