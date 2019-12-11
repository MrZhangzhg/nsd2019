class Role:
    def __init__(self, nm, wp):
        '一般用于绑定属性到对象，不是必须的。self不是关键字，用任何名均可'
        self.name = nm
        self.weapon = wp

if __name__ == '__main__':
    # 实例将会自动作为第一个参数传给方法
    lb = Role('吕布', '方天画戟')  # 自动调用__init__方法
    print(lb.name)
    print(lb.weapon)
