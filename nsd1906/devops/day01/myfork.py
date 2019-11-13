import os

# print('starting...')
# os.fork()
# print('hello world!')

print('starting...')
retval = os.fork()
if retval:
    print('hello from parent')
else:
    print('hello from child')

print('hello from both')



