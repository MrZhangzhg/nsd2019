from random import randint, choice

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def exam():
    '用于出题，让用户作答'
    cmds = {'+': add, '-': sub}
    # 随机选出两个数字并降序排列
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    # 随机选出加减法
    op = choice('+-')

    # 做出正确答案
    # result = cmds[op](nums[0], nums[1])
    result = cmds[op](*nums)

    # 要求用户作答，并判断
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('不错哟！！！')
    else:
        print('不对哟！！！')

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
