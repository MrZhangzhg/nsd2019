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
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:  # 可以捕获所有异常
            print()
            continue

        # 判断对错
        if answer == result:
            print('你真棒!!!')
            break
        print('不对哟')
        counter += 1
    else:
        print('The Anser is: %s%s' % (prompt, result))

def main():
    while True:
        exam()
        # 去除空白字符后取第一个字符
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            yn = 'y'
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()
