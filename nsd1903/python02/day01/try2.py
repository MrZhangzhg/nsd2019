try:
    n = int(input('number: '))
    result = 100 / n
except (ValueError, ZeroDivisionError):
    print('无效输入')
except (EOFError, KeyboardInterrupt):
    print('\nBye-bye')
    exit()  # 程序遇到exit()将会彻底结束，后续代码不再执行
else:
    print(result)
finally:
    print('Done')

print('the end of promgram.')
