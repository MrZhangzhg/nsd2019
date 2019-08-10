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
# 添加数据
# insert = "INSERT INTO departments VALUES(%s, %s)"
# deps = [(1, '人事部'), (2, '运维部'), (3, '开发部'), (4, '测试部'), (5, '市场部'), (6, '销售部')]
# cursor.executemany(insert, deps)
#################################
# 查询并取出查询结果
select = "SELECT * FROM departments"
cursor.execute(select)
result1 = cursor.fetchone()  # 取出一个记录
print(result1)
print('*' * 30)
result2 = cursor.fetchmany(2)  # 取出2个记录
print(result2)
print('*' * 30)
result3 = cursor.fetchall()  # 取出全部记录
print(result3)



#################################
conn.commit()
cursor.close()
conn.close()
