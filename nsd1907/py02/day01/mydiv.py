# try:
#     num = int(input('number: '))
#     result = 100 / num
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
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError):
#     print('无效的输入')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

# try:
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e
#     print('无效的输入:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

# try:
#     num = int(input('number: '))
#     result = 100 / num
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e
#     print('无效的输入:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
#     exit(101)  # 程序遇到exit将会彻底结束
# else:
#     print(result)
#
# print('Done')

try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e
    print('无效的输入:', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(101)  # 程序遇到exit将会彻底结束
else:
    print(result)
finally:
    print('一定要执行的语句')

print('Done')

