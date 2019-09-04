# try:
#     num = int(input("数字: "))
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

#########################################
# try:
#     num = int(input("数字: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError):
#     print('无效的输入')
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

#########################################
# try:
#     num = int(input("数字: "))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError) as e:  # 把异常保存到变量e
#     print('无效的输入: %s' % e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

#########################################
# try:
#     num = int(input("数字: "))
#     result = 100 / num
# except (ValueError, ZeroDivisionError) as e:  # 把异常保存到变量e
#     print('无效的输入: %s' % e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
# else:
#     print(result)
#
# print('Done')

#########################################
try:
    num = int(input("数字: "))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:  # 把异常保存到变量e
    print('无效的输入: %s' % e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit()   # 程序遇到exit，将彻底结束，不会再向下执行
else:
    print(result)
finally:
    print('异常不管是不是发生了，都要执行')

print('Done')

