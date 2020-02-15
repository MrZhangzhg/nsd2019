# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
# except ValueError:
#     print('输入的必须是非0数字')
# except ZeroDivisionError:
#     print('输入的必须是非0数字')
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')
#
# print('Done')

# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
# except (ValueError, ZeroDivisionError):
#     print('输入的必须是非0数字')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
#
# print('Done')

# try:
#     n = int(input('number: '))
#     result = 100 / n
#     print(result)
# except (ValueError, ZeroDivisionError) as e:  # 将报错信息保存到变量e中
#     print('错误:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
#
# print('Done')

try:
    n = int(input('number: '))
    result = 100 / n
except (ValueError, ZeroDivisionError) as e:  # 将报错信息保存到变量e中
    print('错误:', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit()  # 程序遇到exit将会彻底结束
else:  # 异常不发生才执行的语句，放到else中
    print(result)
finally:  # 不管异常是否发生，一定会执行的语句
    print('Done')
