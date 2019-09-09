import threading

def hello():
    print('Hello World!')

if __name__ == '__main__':
    for i in range(3):
        # 生成工作线程
        t = threading.Thread(target=hello)
        # 启动工作线程
        t.start()  # 调用target()


