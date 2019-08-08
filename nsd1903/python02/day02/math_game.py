def exam():


def main():
    "该函数先出题，然后询问用户是否继续"
    while True:
        exam()
        # 去除字符串两端空白字符后，取出第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
