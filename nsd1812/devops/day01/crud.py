from dbconn import Session, Department, Employee, Salary

session = Session()
#################################
# hr = Department(dep_id=1, dep_name='人事部')
# finance = Department(dep_id=2, dep_name='财务部')
# ops = Department(dep_id=3, dep_name='运维部')
# dev = Department(dep_id=4, dep_name='开发部')
# qa = Department(dep_id=5, dep_name='测试部')
# session.add_all([hr, finance, ops, dev, qa])
#################################
# wt = Employee(
#     emp_id=1,
#     emp_name='王涛',
#     email='wangtao@qq.com',
#     dep_id=3
# )
# zj = Employee(
#     emp_id=2,
#     emp_name='张钧',
#     email='zhangjun@163.com',
#     dep_id=3
# )
# sy = Employee(
#     emp_id=3,
#     emp_name='苏艳',
#     email='suyan@qq.com',
#     dep_id=1
# )
# wjy = Employee(
#     emp_id=4,
#     emp_name='吴计印',
#     email='wujiying@126.com',
#     dep_id=4
# )
# kzw = Employee(
#     emp_id=5,
#     emp_name='康志文',
#     email='kangzhiwen@qq.com',
#     dep_id=4
# )
# hzq = Employee(
#     emp_id=6,
#     emp_name='胡志强',
#     email='huzhiqiang@163.com',
#     dep_id=5
# )
# lh = Employee(
#     emp_id=7,
#     emp_name='李浩',
#     email='lihao@126.com',
#     dep_id=2
# )
# session.add_all([wt, zj, sy, wjy, kzw, hzq, lh])
#################################
# qset1 = session.query(Department)
# print(qset1)  # qset1只是个sql语句，当取具体值的时候，才真正查数据库
# # qset1.all()取出全部的部门，因为查询的是类名，所以返回所有的实例组成的列表
# print('*' * 30)
# print(qset1.all())
# print('*' * 30)
# for dep in qset1:  # 遍历实例列表中的每个实例
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#################################
# qset2 = session.query(Department).order_by(Department.dep_id)
# for dep in qset2:  # 遍历实例列表中的每个实例
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#################################
# qset3 = session.query(Employee.emp_name, Employee.email)
# # 查询的参数是字段，返回的结果是元组
# for item in qset3:
#     print(item)
# print('*' * 30)
# for name, email in qset3:
#     print('%s: %s' % (name, email))
#################################
# qset4 = session.query(Department).order_by(Department.dep_id)[1:4]
# for dep in qset4:  # 遍历实例列表中的每个实例
#     print('%s: %s' % (dep.dep_id, dep.dep_name))
#################################
# qset5 = session.query(Department).filter(Department.dep_id==2)
# print(qset5)
# print(qset5.all())  # all()返回列表
# dep = qset5.one()  # 返回一个实例，如果返回值不是一个，将报错
# print(dep.dep_id, dep.dep_name)
#################################
# qset6 = session.query(Department).filter(Department.dep_id>1).filter(Department.dep_id<4)
# for dep in qset6:
#     print(dep.dep_id, dep.dep_name, sep=', ')
#################################
# qset7 = session.query(Employee).filter(Employee.email.like('%@qq.com'))
# for emp in qset7:
#     print(emp.emp_name, emp.email)
#################################
# qset8 = session.query(Department).filter(Department.dep_id.in_([3, 4]))
# for dep in qset8:
#     print(dep.dep_id, dep.dep_name)
#################################
# qset9 = session.query(Department).filter(Department.dep_name.isnot(None))
# for dep in qset9:
#     print(dep.dep_id, dep.dep_name)
#################################
# query中先写的是Employee，join中要写Department
# qset10 = session.query(Employee.emp_name, Department.dep_name).join(Department)
# for row in qset10:
#     print(row)
#################################
# qset11 = session.query(Department.dep_name, Employee.emp_name).join(Employee)
# for row in qset11:
#     print(row)
#################################
# 修改数据，先找到实例，再给实例的属性重新赋值
# qset12 = session.query(Department).filter(Department.dep_name=='人事部')
# hr = qset12.one()
# hr.dep_name='人力资源部'
#################################
# 删除，只要找到实例，然后删除即可
qset13 = session.query(Employee).filter(Employee.emp_id==6)
emp = qset13.one()
session.delete(emp)


#################################
session.commit()
session.close()
