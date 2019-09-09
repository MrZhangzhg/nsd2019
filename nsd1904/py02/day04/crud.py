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
# qset2 = session.query(Employees.emp_name, Employees.email)
# print(qset2.all())  # all方法返回所有结果构成的列表
# for item in qset2:
#     print(item)
##################################
# 排序
# qset3 = session.query(Departments).order_by(Departments.dep_id)[1:3]
# for dep in qset3:
#     print(dep.dep_id, dep.dep_name)
##################################
# 过滤，得到的结果有0或多项的列表
# qset4 = session.query(Departments).filter(Departments.dep_id==3)
# print(qset4.all())
# for dep in qset4:
#     print(dep.dep_id, dep.dep_name)
##################################
# 过滤，可以书写多个条件
# qset5 = session.query(Departments)\
#     .filter(Departments.dep_id>1, Departments.dep_id<4)
# for dep in qset5:
#     print(dep.dep_id, dep.dep_name)
##################################
# 模糊查询
# qset6 = session.query(Employees).filter(Employees.email.like('%@qq.com'))
# for emp in qset6:
#     print(emp.emp_name, emp.email)
##################################
# qset7 = session.query(Departments).filter(Departments.dep_id.in_([1, 3, 6]))
# print(qset7.all())  # all返回列表
# print(qset7.first())   # 返回all列表中的第一项
# dep = qset7.first()
# print(dep.dep_id, dep.dep_name)
##################################
# qset8 = session.query(Departments).filter(Departments.dep_id==3)
# dep = qset8.one() # one要求返回一项，0或多都会报错
# print(dep.dep_id, dep.dep_name)
##################################
# 多表查询，先写Employees.emp_name，join的参数必须是Departments
# 如果写先Departments.dep_name，join的参数必须是Employees
# qset9 = session.query(Employees.emp_name, Departments.dep_name)\
#     .join(Departments)
# print(qset9.all())
##################################
# 修改，只要进行变量重新赋值即可
# qset10 = session.query(Departments).filter(Departments.dep_id==1)
# hr = qset10.one()
# hr.dep_name = '人力资源部'
##################################
# 删除，先取出实例，再调用delete方法
qset11 = session.query(Departments).filter(Departments.dep_id==6)
market = qset11.one()
session.delete(market)



##################################
session.commit()
session.close()
