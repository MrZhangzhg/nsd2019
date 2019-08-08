from random import randint, choice

def exam():
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')   # 随机选择加减号
    # 计算出正确答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    # 让用户做答，判断对错
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('非常棒!!!')
    else:
        print('不对哟!!!')

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
