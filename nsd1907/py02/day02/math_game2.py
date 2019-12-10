from random import choice, randint

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    '出题测试'
    cmds = {'+': add, '-': sub}
    # 随机取出100以内的两个随机数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列

    # 随机取出加减法
    op = choice('+-')

    # 算出正确答案
    # result = cmds[op](nums[0], nums[1])
    result = cmds[op](*nums)

    # 用户作答
    counter = 0
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:  # 不指定具体的异常，可以捕获全部异常，不推荐
            print()
            continue

        if answer == result:
            print('Very Good!!!')
            break
        else:
            print('Wrong Anwswer!!!')
        counter += 1
    else:
        print('\033[31;1m%s%s\033[0m' % (prompt, result))


def main():
    while 1:
        exam()
        # 将用户输入信息的额外空白字符删除后，取出第一个字符
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
