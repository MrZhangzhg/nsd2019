from random import randint, choice


def exam():
    nums = [randint(1, 100) for i in range(2)]  # 生成两个数字的列表
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')   # 随机选加减法
    # 计算出正确答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    # 让用户作答
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    # 判断对错
    if answer == result:
        print('你真棒!!!')
    else:
        print('不对哟')

def main():
    while True:
        exam()
        # 去除空白字符后取第一个字符
        yn = input('Continue(y/n)? ').strip()[0]
        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
