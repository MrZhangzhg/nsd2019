try:
    nums = int(input('number: '))
    result = 100 / nums
    print(result)
except ValueError:
    print('无效输入')

print('Done')
