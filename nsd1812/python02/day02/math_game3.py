from random import randint, choice

def exam():
    cmds = {'+': lambda x, y: x + y, '-': lambda x, y: x - y}
    nums = [randint(1, 100) for i in range(2)]  # 生成两个数字
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')
    result = cmds[op](*nums)

    prompt = '%s %s %s = ' % (nums[0], op, nums[1])  # 5 + 3 =
    counter = 0

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue

        if answer == result:
            print('Very Good!!!')
            break

        print('Wrong Answer!!!')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

if __name__ == '__main__':
    while True:
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
