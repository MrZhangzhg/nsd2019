def exam():
    print('exam')


if __name__ == '__main__':
    while True:
        exam()
        # 删除用户输入的多余空格，并取出第1个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break
