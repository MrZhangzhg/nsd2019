# 1 + 1 = 2
# very good
# Continue(y/n)? y
# 12+23 = 1
# wrong
# 12 + 23 = 2
# wrong
# 12 + 23 = 3
# wrong
# 12 + 23 = 35
# Continue(y/n)? n
# Bye-bye

from random import randint, choice

def exam():
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)  # 降序排列
    op = choice('+-')  # 随机选+-
    # 算出正确答案
    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    # 用户答题
    prompt = '%s %s %s = ' % (nums[0], op, nums[1])
    answer = int(input(prompt))
    if answer == result:
        print('太棒了！！！')
    else:
        print('不对哟！')

def main():
    while 1:
        exam()
        try:
            yn = input('Continue(y/n)? ').strip()[0]  # 取出第一个字符
        except IndexError:  # 空白字符导致的异常，认为用户要继续
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'

        if yn in 'nN':
            print('\nBye-bye')
            break

if __name__ == '__main__':
    main()





