
def exam():
    '出题测试'


def main():
    while 1:
        exam()
        # 将用户输入信息的额外空白字符删除后，取出第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
