try:
    num = int(input('number: '))
    result = 100 / num
    print(result)
    print('Done')
except ValueError:
    print('只接受数字')
except ZeroDivisionError:
    print('0不能作除数')
except KeyboardInterrupt:
    print('\nBye-bye')
except EOFError:
    print('\nBye-bye')

