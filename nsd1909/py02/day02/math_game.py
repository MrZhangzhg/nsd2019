def exam():
    '用于出题，让用户作答'
    print('exam')

def main():
    '类似于以前的show_menu，用于展示主程序代码'
    while 1:
        exam()
        # 将用户输入的字符串去掉两端空格后，取第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
