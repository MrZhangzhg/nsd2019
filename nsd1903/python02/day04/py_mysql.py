import pymysql

# 建立连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1903',
    charset='utf8'
)

# 创建操作数据库的游标
cursor = conn.cursor()

# 编写创建表的SQL语句
create_dep = """CREATE TABLE departments(
dep_id INT, dep_name VARCHAR(20),
PRIMARY KEY(dep_id)
)"""
create_emp = """CREATE TABLE employees(
emp_id INT, emp_name VARCHAR(20), birth_date DATE, email VARCHAR(50),
dep_id INT,
PRIMARY KEY(emp_id), FOREIGN KEY(dep_id) REFERENCES departments(dep_id)
)"""
create_salay = """CREATE TABLE salary(
id INT, date DATE, emp_id INT, basic INT, awards INT,
PRIMARY KEY(id), FOREIGN KEY(emp_id) REFERENCES employees(emp_id)
)"""

# 通过cursor执行SQL语句
cursor.execute(create_dep)
cursor.execute(create_emp)
cursor.execute(create_salay)

# 确认
conn.commit()

# 关闭
cursor.close()
conn.close()
