# 1 + 1 = 2
# very good
# Continue(y/n)? y
# 12+23 = 1
# wrong
# 12 + 23 = 2
# wrong
# 12 + 23 = 3
# wrong
# 12 + 23 = 35
# Continue(y/n)? n
# Bye-bye

def exam():
    print('exam')

def main():
    while 1:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]  # 取出第一个字符
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()





