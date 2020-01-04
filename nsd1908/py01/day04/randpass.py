from random import choice

all_chs = '1234567890qwertyuiopasdfghjklZxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
result = ''

for i in range(8):
    ch = choice(all_chs)
    result += ch

print(result)
