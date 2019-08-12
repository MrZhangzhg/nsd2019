import time
import threading

def hello(a, b):
    time.sleep(3)
    print('Hello', a, b)

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=hello, args=('aaa', 'bbb'))
        t.start()   # 启动工作线程，调用target(*args)
