try:
    n = int(input('number: '))
    result = 100 / n
except (ValueError, ZeroDivisionError) as e:  # 把异常保存到变量e中
    print('无效的输入:', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit()  # 程序遇到exit就彻底结束
else:
    print(result)
finally:
    print('Done')

print('结束')
