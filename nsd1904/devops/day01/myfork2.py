import os

print('starting')
retval = os.fork()
# retval在父进程中的值是非0值（子进程的ID号），子进程中是0
print(retval)

if retval:
    print('in parent')
else:
    print('in child')
