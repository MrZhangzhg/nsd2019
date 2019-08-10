import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1903',
    charset='utf8'
)
cursor = conn.cursor()
#################################
insert = "INSERT INTO departments VALUES(%s, %s)"
deps = [(1, '人事部'), (2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '市场部'), (6, '销售部')]
cursor.executemany(insert, deps)

#################################
conn.commit()
cursor.close()
conn.close()
