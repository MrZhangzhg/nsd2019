from dbconn import Departments, Employees, Session

#######################################
# 创建到数据库连接的会话
session = Session()
#######################################
# 增加记录就是创建类的实例
# hr = Departments(dep_id=1, dep_name='人事部')
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# sales = Departments(dep_id=5, dep_name='销售部')
# market = Departments(dep_id=6, dep_name='市场部')
# session.add_all([hr, ops, dev, qa, sales, market])
#######################################
# 增加员工
# lb = Employees(
#     emp_id=1, emp_name='刘备',
#     birth_date='1975-03-18', email='lb@qq.com', dep_id=1
# )
# gy = Employees(
#     emp_id=2, emp_name='关羽',
#     birth_date='1980-2-15', email='gy@qq.com', dep_id=2
# )
# zf = Employees(
#     emp_id=3, emp_name='张飞',
#     birth_date='1982-10-3', email='zf@qq.com', dep_id=2
# )
# zy = Employees(
#     emp_id=4, emp_name='赵云',
#     birth_date='1995-4-19', email='zy@163.com', dep_id=2
# )
# hz = Employees(
#     emp_id=5, emp_name='黄忠',
#     birth_date='1970-1-1', email='hz@126.com', dep_id=3
# )
# wy = Employees(
#     emp_id=6, emp_name='魏严',
#     birth_date='1993-6-13', email='wy@163.com', dep_id=3
# )
# session.add_all([lb, gy, zf, zy, hz, wy])
#######################################
# 查询时，将类作为参数，返回的是实例集合
qset1 = session.query(Departments)
# print(qset1)   # qset1是SQL语句，取值时sql语句才会执行，返回结果
for dep in qset1:
    print(dep.dep_id, dep.dep_name)
#######################################
# 查询时，将类变量作为参数，返回的是元组构成的查询集
qset2 = session.query(Departments.dep_id, Departments.dep_name)
for dep in qset2:
    print(dep)


#######################################
session.commit()   # 确认
session.close()    # 关闭会诂连接
