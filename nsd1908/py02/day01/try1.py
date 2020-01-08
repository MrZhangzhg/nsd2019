try:
    num = int(input('number: '))
    result = 100 / num
    print(result)
    print('Done')
except ValueError:
    print('只接受数字')
