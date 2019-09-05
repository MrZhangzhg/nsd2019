def exam():
    "出题，用户作答"


def main():
    "调用出题函数，控制程序是否继续运行"
    while True:
        exam()
        # 将用户输入的两端空白字符删除，再取出第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':  # 只有yn的值是n或N才退出，否则全继续
            print('\nBye-bye')
            break


if __name__ == '__main__':
    main()
