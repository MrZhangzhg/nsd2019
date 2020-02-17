from random import randint, choice

def exam():
    '用于出题，让用户作答'
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    # 随机选出两个数字并降序排列
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    # 随机选出加减法
    op = choice('+-')

    # 做出正确答案
    # result = cmds[op](nums[0], nums[1])
    result = cmds[op](*nums)

    # 要求用户作答，并判断
    counter = 0   # 计数器，用于计录用户作答次数
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    while counter < 3:
        try:
            answer = int(input(prompt))
        except:   # except后面不指定具体的异常，可以捕获所有异常，不推荐
            print()
            continue

        if answer == result:
            print('不错哟！！！')
            break
        print('不对哟！！！')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    '类似于以前的show_menu，用于展示主程序代码'
    while 1:
        exam()
        # 将用户输入的字符串去掉两端空格后，取第一个字符
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'  # 当用户按下ctrl+c或ctrl+d时，算他输入n

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
