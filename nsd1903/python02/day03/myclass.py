class GameRole:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是%s, 我的武器是%s' % (self.name, self.weapon))

    def speak(self, content):
        print('%s在此, %s' % (self.name, content))

    def attack(self, dest):
        print('正在攻击: %s' % dest)

if __name__ == '__main__':
    # 创建实例时，自动调用__init__方法
    # 调用通过类创建的方法，实例自动作为第一个参数传递
    lb = GameRole('吕布', '方天画戟')  # 创建名为lb的实例
    print(lb.name, lb.weapon)
    lb.show_me()
    lb.speak('人在塔在')

    zf = GameRole('张飞', '丈八蛇矛')
    zf.show_me()
    zf.speak('燕人张飞')

    zf.attack('吕布')
    lb.attack('刘备')
