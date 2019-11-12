class Warrior:
    def __init__(self, name, weapon):
        'self不是关键字，可以是任何名字，表示实例本身'
        # 绑定在对象身上的属性，在类中任意位置可用
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        # 方法自己的参数、变量就是函数的局部变量
        print('我是%s, %s' % (self.name, words))

    def attack(self, target):
        print('正在攻击: %s' % target)

if __name__ == '__main__':
    # 创建实例时，自动调用__init__方法，实例自动作为第一个参数
    lb = Warrior('吕布', '方天画戟')  # 创建实例
    print(lb.name)
    print(lb.weapon)
    lb.speak('马中赤兔，人中吕布')
    print('*' * 30)
    zf = Warrior('张飞', '丈八蛇矛')
    print(zf.name, zf.weapon)
    zf.speak('我是燕人张飞张冀德')
    print('*' * 30)
    lb.attack('董卓')
    zf.attack('吕布')
