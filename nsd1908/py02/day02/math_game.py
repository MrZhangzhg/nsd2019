from random import randint, choice

def exam():
    '用于出题，让用户作答'
    # 随机生成两个数字
    nums = [randint(1, 100) for i in range(2)]
    # 降序排列
    nums.sort(reverse=True)
    # 随机选出加减法
    op = choice('+-')

    # 计算出正确答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    # 要求用户作答，并判断正误
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('Very Good!!!')
    else:
        print('不对哟!!!')

def main():
    while 1:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]  # 取第一个字符
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
