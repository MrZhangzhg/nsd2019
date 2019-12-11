class Role:
    def __init__(self, nm, wp):
        '一般用于绑定属性到对象，不是必须的。self不是关键字，用任何名均可'
        # 绑定在实例身上的属性，可以在class中的任何位置使用
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是%s, 我使用%s' % (self.name, self.weapon))

    def speak(self, words):
        # 没有绑在实例身上的变量words就是函数的局部变量
        print(words)

if __name__ == '__main__':
    # 实例将会自动作为第一个参数传给方法
    lb = Role('吕布', '方天画戟')  # 自动调用__init__方法
    print(lb.name)
    print(lb.weapon)
    lb.show_me()
    lb.speak('马中赤兔，人中吕布!')
