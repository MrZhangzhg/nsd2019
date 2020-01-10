class Role:
    def __init__(self, name, weapon):
        "__init__是构造器方法，创建实例时，它自动调用，一般用于将属性绑到对象"
        self.name = name
        self.weapon = weapon

if __name__ == '__main__':
    # 实例化时，实例名lb将自动作为第一个参数，传给相关的方法
    lb = Role('吕布', '方天画戟')
    print(lb.name, lb.weapon)
