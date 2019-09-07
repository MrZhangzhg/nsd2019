import pymysql

# 创建到数据的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1904',
    charset='utf8'
)

cur = conn.cursor()  # 创建游标，相当于文件对象
###################################
# 编写创建表的SQL语句
create_dep = """CREATE TABLE departments(
dep_id INT, dep_name VARCHAR(20),
PRIMARY KEY(dep_id)
)"""

create_emp = """CREATE TABLE employees(
emp_id INT, emp_name VARCHAR(20), birth_date DATE,
email VARCHAR(50), dep_id INT,
PRIMARY KEY(emp_id),
FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
)"""

create_sal = """CREATE TABLE salary(
id INT, date DATE, emp_id INT, basic INT, awards INT,
PRIMARY KEY(id),
FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)"""
# 执行SQL语句
cur.execute(create_dep)
cur.execute(create_emp)
cur.execute(create_sal)
###################################
conn.commit()
cur.close()
conn.close()
