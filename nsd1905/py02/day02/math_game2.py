from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    cmds = {'+': add, '-': sub}
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')  # 随机选+-
    # 算出正确答案
    result = cmds[op](*nums)

    # 用户答题
    counter = 0
    while counter < 3:
        prompt = '%s %s %s = ' % (nums[0], op, nums[1])
        try:
            answer = int(input(prompt))
        except:  # 不写异常，可以捕获所有异常，不推荐
            print()
            continue

        if answer == result:
            print('太棒了！！！')
            break

        print('不对哟！')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    while 1:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]  # 取出第一个字符
        except IndexError:  # 空白字符导致的异常，认为用户要继续
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()





