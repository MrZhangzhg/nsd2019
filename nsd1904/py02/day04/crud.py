from dbconn import Session, Departments, Employees, Salary

# 创建会话实例，将来对数据库实现增删改查，都是通过session的方法实现
session = Session()
##################################
# 创建部门
hr = Departments(dep_id=1, dep_name='人事部')
finance = Departments(dep_id=2, dep_name='财务部')
ops = Departments(dep_id=3, dep_name='运维部')
dev = Departments(dep_id=4, dep_name='开发部')
qa = Departments(dep_id=5, dep_name='测试部')
market = Departments(dep_id=6, dep_name='市场部')

session.add_all([hr, finance, ops, dev, qa, market])




##################################
session.commit()
session.close()
