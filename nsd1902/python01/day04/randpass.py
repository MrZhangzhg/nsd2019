from random import choice

chs = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'
result = ''

for i in range(8):
    ch = choice(chs)
    result += ch

print(result)
