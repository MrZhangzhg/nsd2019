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
    counter = 0
    while counter < 3:
        try:
            answer = int(input(prompt))
        except:  # 可以捕获所有异常，但是不推荐
            print()
            continue

        if answer == result:
            print('Very Good!!!')
            break
        print('不对哟!!!')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    while 1:
        exam()
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
