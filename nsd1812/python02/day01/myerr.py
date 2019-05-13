try:
    nums = int(input('number: '))
    result = 100 / nums
    print(result)
except ValueError:
    print('无效输入')
    exit(1)
except ZeroDivisionError:
    print('无效输入')
    exit(1)
except KeyboardInterrupt:
    print('\nBye-bye')
    exit(2)
except EOFError:
    print('\nBye-bye')
    exit(2)

print('Done')
