import pymysql

# 建立到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1', port=3306,
    user='root', passwd='tedu.cn',
    db='nsd1908', charset='utf8'
)

# 创建游标，它就像文件对象一样
cur = conn.cursor()

# 编写SQL语句
mk_dep = """CREATE TABLE departments(
dep_id INT, dep_name VARCHAR(50),
PRIMARY KEY(dep_id)
)"""
mk_emp = """CREATE TABLE employees(
emp_id INT, emp_name VARCHAR(20), email VARCHAR(50), dep_id INT,
PRIMARY KEY(emp_id),
FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
)"""
mk_sal = """CREATE TABLE salary(
id INT, date DATE, emp_id INT, basic INT, awards INT,
PRIMARY KEY(id),
FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)"""

# 执行SQL语句
cur.execute(mk_dep)
cur.execute(mk_emp)
cur.execute(mk_sal)
# 确认
conn.commit()

# 关闭游标、关闭连接
cur.close()
conn.close()
