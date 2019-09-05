from random import randint, choice


def exam():
    "出题，用户作答"
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')
    result = cmds[op](*nums)

    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:  # 不填写异常，可以捕获所有异常。不推荐
            print()
            continue

        if answer == result:
            print('不错哟！')
            break

        print('\033[31;1m不对哟！\033[0m')
        counter += 1
    else:
        print('%s%s' % (prompt, result))


def main():
    "调用出题函数，控制程序是否继续运行"
    while True:
        exam()
        # 将用户输入的两端空白字符删除，再取出第一个字符
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':  # 只有yn的值是n或N才退出，否则全继续
            print('\nBye-bye')
            break


if __name__ == '__main__':
    main()
