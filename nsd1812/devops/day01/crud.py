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
wt = Employee(
    emp_id=1,
    emp_name='王涛',
    email='wangtao@qq.com',
    dep_id=3
)
zj = Employee(
    emp_id=2,
    emp_name='张钧',
    email='zhangjun@163.com',
    dep_id=3
)
sy = Employee(
    emp_id=3,
    emp_name='苏艳',
    email='suyan@qq.com',
    dep_id=1
)
wjy = Employee(
    emp_id=4,
    emp_name='吴计印',
    email='wujiying@126.com',
    dep_id=4
)
kzw = Employee(
    emp_id=5,
    emp_name='康志文',
    email='kangzhiwen@qq.com',
    dep_id=4
)
hzq = Employee(
    emp_id=6,
    emp_name='胡志强',
    email='huzhiqiang@163.com',
    dep_id=5
)
lh = Employee(
    emp_id=7,
    emp_name='李浩',
    email='lihao@126.com',
    dep_id=2
)
session.add_all([wt, zj, sy, wjy, kzw, hzq, lh])




#################################
session.commit()
session.close()
