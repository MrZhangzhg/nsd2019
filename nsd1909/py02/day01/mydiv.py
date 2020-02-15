try:
    n = int(input('number: '))
    result = 100 / n
    print(result)
except ValueError:
    print('输入的必须是非0数字')
except ZeroDivisionError:
    print('输入的必须是非0数字')
except KeyboardInterrupt:
    print('\nBye-bye')
except EOFError:
    print('\nBye-bye')
