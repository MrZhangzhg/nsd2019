from dbconn import Departments, Employees, Salary, Session

# 创建会话实例，用于连接数据库
session = Session()

# 创建部门实例
hr = Departments(dep_id=1, dep_name='人事部')
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qa = Departments(dep_id=4, dep_name='测试部')
finance = Departments(dep_id=5, dep_name='财务部')
market = Departments(dep_id=6, dep_name='市场部')
sales = Departments(dep_id=7, dep_name='销售部')

# 在数据库中创建记录
deps = [hr, ops, dev, qa, finance, market, sales]
session.add_all(deps)
session.commit()   # 确认至数据库

# 关闭会话
session.close()
