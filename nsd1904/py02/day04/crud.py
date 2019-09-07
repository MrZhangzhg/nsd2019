from dbconn import Session, Departments, Employees, Salary

# 创建会话实例，将来对数据库实现增删改查，都是通过session的方法实现
session = Session()
##################################
# 创建部门
# hr = Departments(dep_id=1, dep_name='人事部')
# finance = Departments(dep_id=2, dep_name='财务部')
# ops = Departments(dep_id=3, dep_name='运维部')
# dev = Departments(dep_id=4, dep_name='开发部')
# qa = Departments(dep_id=5, dep_name='测试部')
# market = Departments(dep_id=6, dep_name='市场部')
# session.add_all([hr, finance, ops, dev, qa, market])
##################################
# 创建员工
# lb = Employees(
#     emp_id=1, emp_name='刘备', birth_date='1970-9-10',
#     email='lb@shu.com', dep_id=1
# )
# zgl = Employees(
#     emp_id=2, emp_name='诸葛亮', birth_date='1973-8-9',
#     email='zgl@qq.com', dep_id=2
# )
# gy = Employees(
#     emp_id=3, emp_name='关羽', birth_date='1990-5-12',
#     email='gy@qq.com', dep_id=3
# )
# zf = Employees(
#     emp_id=4, emp_name='张飞', birth_date='1991－4－18',
#     email='zf@163.com', dep_id=3
# )
# zy = Employees(
#     emp_id=5, emp_name='赵云', birth_date='1995-7-23',
#     email='zy@qq.com', dep_id=4
# )
# session.add_all([lb, zgl, gy, zf, zy])
##################################
# 把类作为参数，得到的是实例列表
# qset1 = session.query(Departments)
# print(qset1)  # 此时，qset1只是一条sql语句
# for dep in qset1:
#     print(dep.dep_id, dep.dep_name)
##################################
# 把类变量作为参数，得到是元组的列表
qset2 = session.query(Employees.emp_name, Employees.email)
print(qset2.all())  # all方法返回列表
for item in qset2:
    print(item)




##################################
session.commit()
session.close()
