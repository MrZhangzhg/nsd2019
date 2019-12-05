import random

all_chs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

result = ''
for i in range(8):
    ch = random.choice(all_chs)
    result += ch

print(result)
