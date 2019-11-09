from random import randint, choice

def exam():
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')
    # 计算标准答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    # 提示语，即算式
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))

    if answer == result:
        print('Very Good!!!')
    else:
        print('不对哟!!!')

def main():
    while 1:
        exam()
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
