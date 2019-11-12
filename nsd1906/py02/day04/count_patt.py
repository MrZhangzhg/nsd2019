
def count_patt(fname, patt):



if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 12345.6789.1.232, 10.123.45.8
    br = 'Firefox|MSIE|Chrome'
    result1 = count_patt(fname, ip)
    result2 = count_patt(fname, br)
    print(result1)
    print(result2)
