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
# 添加部门
insert_dep = 'INSERT INTO departments(dep_id, dep_name) VALUES(%s, %s)'
hr = [(1, '人事部')]
deps = [(2, '财务部'), (3, '运维部'), (4, '开发部'), (5, '测试部'), (6, '市场部')]
cur.executemany(insert_dep, hr)
cur.executemany(insert_dep, deps)
###################################
conn.commit()
cur.close()
conn.close()
