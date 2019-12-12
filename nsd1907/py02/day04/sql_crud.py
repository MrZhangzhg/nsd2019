# create / retrieve / update / delete
from dbconn import Session, Departments, Employees

# 创建到数据库的会话连接
session = Session()

# 插入数据
# hr = Departments(dep_id=1, dep_name='人事部')
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# sales = Departments(dep_id=5, dep_name='销售部')
# market = Departments(dep_id=6, dep_name='市场部')
# session.add_all([hr, ops, dev, qa, sales, market])

# lb = Employees(
#     emp_id=1, emp_name='刘备',
#     birth_date='1982-3-15', email='lb@tedu.cn', dep_id=1
# )
# km = Employees(
#     emp_id=2, emp_name='孔明',
#     birth_date='1983-8-22', email='km@qq.com', dep_id=1
# )
# zf = Employees(
#     emp_id=3, emp_name='张飞',
#     birth_date='1988-10-1', email='zf@tedu.cn', dep_id=2
# )
# gy = Employees(
#     emp_id=4, emp_name='关羽',
#     birth_date='1986-7-19', email='gy@163.com', dep_id=3
# )
# session.add_all([lb, km, zf, gy])

# 查询部门，传入的是class，返回的是实例集合
# qset1 = session.query(Departments)
# print(qset1)  # 此时只是sql语句，取值时，才真正连接数据库
# print(qset1.all())
# for dep in qset1:
#     print(dep.dep_id, dep.dep_name)

# 查询员工，传入的是字段，返回的是由字段构成的元组
# qset2 = session.query(Employees.emp_name, Employees.email)
# print(qset2)
# for data in qset2:
#     print(data)
# print('*' * 30)
# for name, email in qset2:
#     print(name, email)

# 查询部门，按id排序
# qset3 = session.query(Departments).order_by(Departments.dep_id)
# for dep in qset3:
#     print(dep.dep_id, dep.dep_name)

# 查询部门id是1的部门
# qset4 = session.query(Departments).filter(Departments.dep_id==1)
# for dep in qset4:
#     print(dep.dep_id, dep.dep_name)

# 查询部门id是2到4的部门
# qset5 = session.query(Departments)\
#     .filter(Departments.dep_id>=2)\
#     .filter(Departments.dep_id<5)
# for dep in qset5:
#     print(dep.dep_id, dep.dep_name)

# 模糊查询
# qset6 = session.query(Employees.emp_name, Employees.email)\
#     .filter(Employees.email.like('%@tedu.cn'))
# for emp in qset6:
#     print(emp.emp_name, emp.email)

# 多表查询。query查询的时候，先写Employees.emp_name，就要join Departments
# qset7 = session.query(Employees.emp_name, Departments.dep_name)\
#     .join(Departments)
# for data in qset7:
#     print(data)

# qset8 = session.query(Departments.dep_name, Employees.emp_name)\
#     .join(Employees)
# for data in qset8:
#     print(data)

# 修改
# qset9 = session.query(Departments)\
#     .filter(Departments.dep_name=='人事部')
# hr = qset9.first()  # 取出查询结果的第一项
# print(hr)
# hr.dep_name = '人力资源部'

# 删除
qset10 = session.query(Departments)\
    .filter(Departments.dep_name=='销售部')
sales = qset10[0]
print(sales)
session.delete(sales)

# 如果是增删改操作，需要确认commit
session.commit()

# 关闭会话
session.close()
