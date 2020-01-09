def exam():
    '用于出题，让用户作答'

def main():
    while 1:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]  # 取第一个字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
