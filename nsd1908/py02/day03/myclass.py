class Role:
    def __init__(self, name, weapon):
        "__init__是构造器方法，创建实例时，它自动调用，一般用于将属性绑到对象"
        self.name = name
        self.weapon = weapon

    def show_me(self):
        "绑定在实例上的属性，在任意方法中都直接可用"
        print("我是%s, 我的兵器是%s" % (self.name, self.weapon))

    def say(self, words):
        "没有绑定的变量，是临时变量"
        print(words)

if __name__ == '__main__':
    # 实例化时，实例名lb将自动作为第一个参数，传给相关的方法
    lb = Role('吕布', '方天画戟')
    print(lb.name, lb.weapon)
    lb.show_me()
    lb.say('马中赤兔，人中吕布')

    zf = Role('张飞', '丈八蛇矛')
    zf.show_me()
