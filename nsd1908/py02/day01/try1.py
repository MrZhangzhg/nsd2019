# try:
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
#     print('Done')
# except ValueError:
#     print('只接受数字')
# except ZeroDivisionError:
#     print('0不能作除数')
# except KeyboardInterrupt:
#     print('\nBye-bye')
# except EOFError:
#     print('\nBye-bye')

# try:
#     num = int(input('number: '))
#     result = 100 / num
#     print(result)
#     print('Done')
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e中
#     print('只接受非0数字:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')

# try:
#     num = int(input('number: '))
#     result = 100 / num
# except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e中
#     print('只接受非0数字:', e)
# except (KeyboardInterrupt, EOFError):
#     print('\nBye-bye')
#
# print(result)
# print('Done')

try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:  # 将异常保存到变量e中
    print('只接受非0数字:', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(101)  # 程序遇到exit将会结束，101是退出码，即$?
else:  #　异常不发生才会执行的语句放到else中
    print(result)
finally:  # 不管异常是否发生，都会执行的语句发到finally
    print('Done')

##################


# f = open('xxxx')
# try:
#     f.read(10)
# finally:
#     f.close()



