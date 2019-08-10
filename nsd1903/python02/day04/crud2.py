from dbconn import Departments, Employees, Session

#######################################
# 创建到数据库连接的会话
session = Session()
#######################################
# 增加记录就是创建类的实例
hr = Departments(dep_id=1, dep_name='人事部')
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qa = Departments(dep_id=4, dep_name='测试部')
sales = Departments(dep_id=5, dep_name='销售部')
market = Departments(dep_id=6, dep_name='市场部')
session.add_all([hr, ops, dev, qa, sales, market])


#######################################
session.commit()   # 确认
session.close()    # 关闭会诂连接
