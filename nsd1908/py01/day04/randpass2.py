from random import choice
from string import ascii_letters, digits

all_chs = ascii_letters + digits

def randpass(n=8):
    result = ''

    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    print(randpass())
    print(randpass(6))
