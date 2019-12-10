from random import choice, randint

def exam():
    '出题测试'
    # 随机取出100以内的两个随机数字
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列

    # 随机取出加减法
    op = choice('+-')

    # 算出正确答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    # 用户作答
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('Very Good!!!')
    else:
        print('Wrong Anwswer!!!')


def main():
    while 1:
        exam()
        # 将用户输入信息的额外空白字符删除后，取出第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
