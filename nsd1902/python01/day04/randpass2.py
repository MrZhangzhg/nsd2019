from random import choice
from string import ascii_letters, digits

chs = ascii_letters + digits

def gen_pass(n=8):
    result = ''

    for i in range(n):
        ch = choice(chs)
        result += ch

    return result

if __name__ == '__main__':
    pw = gen_pass()
    print(pw)
    print(gen_pass(4))
