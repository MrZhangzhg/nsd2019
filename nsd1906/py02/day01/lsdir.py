import sys
import os

def lsdir(directory):
    for path, folder, files in os.walk(directory):
        print('%s:' % path)
        for d in folder:
            print('\033[34;1m%s\t\033[0m' % d, end='')
        for file in files:
            print('%s\t' % file, end='')
        print('\n')

if __name__ == '__main__':
    lsdir(sys.argv[1])
