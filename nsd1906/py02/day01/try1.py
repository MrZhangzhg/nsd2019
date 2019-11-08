# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
#     print('Done')
# except ValueError:
#     print('无效的输入')
# except ZeroDivisionError:
#     print('无效的输入')
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')


# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
#     print('Done')
# 将异常保存到变量e中
# except (ValueError, ZeroDivisionError) as e:
#     print('无效的输入:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')


try:
    n = int(input('number: '))
    result = 100 / n
except (ValueError, ZeroDivisionError) as e:
    print('无效的输入:', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit()
else:
    print(result)
finally:
    print('异常处理结束')

print('Done')
