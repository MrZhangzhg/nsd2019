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
    counter = 0
    while counter < 3:
        try:
            answer = int(input(prompt))
        except:    # 不指定异常可以捕获所有异常，但是不推荐
            print()
            continue

        if answer == result:
            print('非常棒!!!')
            break
        print('不对哟!!!')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    "该函数先出题，然后询问用户是否继续"
    while True:
        exam()
        # 去除字符串两端空白字符后，取出第一个字符
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
