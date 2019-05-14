from random import randint, choice

def exam():
    nums = [randint(1, 100) for i in range(2)]  # 生成两个数字
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    prompt = '%s %s %s = ' % (nums[0], op, nums[1])  # 5 + 3 =
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:   # 不指定异常可以捕获所有异常，但是不推荐
            print()
            continue

        if answer == result:
            print('Very Good!!!')
            break

        print('Wrong Answer!!!')
        counter += 1
    else:  # 三次全答错，才会输出正确答案
        print('%s%s' % (prompt, result))

if __name__ == '__main__':
    while True:
        exam()
        # 删除用户输入的多余空格，并取出第1个字符
        try:
            yn = input('Continue(y/n)? ').strip()[0]
        except IndexError:
            yn = 'y'
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break
