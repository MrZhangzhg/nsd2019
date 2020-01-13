# import os
#
# print('starting...')
# os.fork()
# print('Hello World!')


# import os
#
# print('starting...')
# ret_val = os.fork()
# if ret_val:
#     print('Hello from parent')
# else:
#     print('Hello from child')
#
# print('Hello World!')


import os

print('starting...')

for i in range(3):
    rev_val = os.fork()
    if not rev_val:
        print('Hello World!')
        exit()

print('Done')











