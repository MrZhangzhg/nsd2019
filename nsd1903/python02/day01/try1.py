try:
    n = int(input('number: '))
    result = 100 / n
    print(result)
except ValueError:
    print('无效输入')
except ZeroDivisionError:
    print('无效输入')
except EOFError:
    print('\nBye-bye')
    exit()  # 程序遇到exit()将会彻底结束，后续代码不再执行
except KeyboardInterrupt:
    print('\nBye-bye')
    exit()

print('Done')
