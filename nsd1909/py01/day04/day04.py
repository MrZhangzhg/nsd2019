def shi_shuzi(s):
    for zifu in s:
        if not zifu in '1234567890':
            print('不全是数字')
            break
    else:
        print('全是数字')

if __name__ == '__main__':
    s = input('number: ')
    shi_shuzi(s)
