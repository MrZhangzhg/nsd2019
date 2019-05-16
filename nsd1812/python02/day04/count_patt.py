
def count_patt(fname, patt):


if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'   # 192.168.1.23, 12345.67890.1.132234354
    br = 'Firefox|MSIE|Chrome'
    print(count_patt(fname, ip))
    print(count_patt(fname, br))
