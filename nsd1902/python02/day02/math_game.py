def exam():
    print('exam')

def main():
    while True:
        exam()
        # 去除空白字符后取第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
