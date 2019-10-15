class Role:
    def __init__(self, nm, wp):
        '构造器方法，创建实例时自动调用，经常用于设置实例属性'
        # 将属性绑定到实例，在类中任意位置可用
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是: %s，擅用%s' % (self.name, self.weapon))

if __name__ == '__main__':
    # 实例化时，自动调用__init__方法，实例自动作为第一个参数
    lb = Role('吕布', '方天画戟')
    print(lb.name)
    print(lb.weapon)
    zf = Role('张飞', '丈八蛇矛')
    print(zf.name)
    print(zf.weapon)
    lb.show_me()   # 调用方法，实例自动作为第一个参数传递
    zf.show_me()
