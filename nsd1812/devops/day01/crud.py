from dbconn import Session, Department, Employee, Salary

session = Session()
#################################
hr = Department(dep_id=1, dep_name='人事部')
finance = Department(dep_id=2, dep_name='财务部')
ops = Department(dep_id=3, dep_name='运维部')
dev = Department(dep_id=4, dep_name='开发部')
qa = Department(dep_id=5, dep_name='测试部')
session.add_all([hr, finance, ops, dev, qa])

#################################

session.commit()
session.close()
