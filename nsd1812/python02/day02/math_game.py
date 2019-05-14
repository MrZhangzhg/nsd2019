from random import randint, choice

def exam():
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('Very Good!!!')
    else:
        print('Wrong Answer!!!')


if __name__ == '__main__':
    while True:
        exam()
        # 删除用户输入的多余空格，并取出第1个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break
