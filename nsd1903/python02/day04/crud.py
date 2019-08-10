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
# select = "SELECT * FROM departments"
# cursor.execute(select)
# result1 = cursor.fetchone()  # 取出一个记录
# print(result1)
# print('*' * 30)
# result2 = cursor.fetchmany(2)  # 取出2个记录
# print(result2)
# print('*' * 30)
# result3 = cursor.fetchall()  # 取出全部记录
# print(result3)
#################################
# 移动游标
# select = "SELECT * FROM departments ORDER BY dep_id"
# cursor.execute(select)
# cursor.scroll(2, mode='absolute')  # 绝对移动，从开头移动2条记录
# result1 = cursor.fetchone()
# print(result1)
# print('*' * 30)
# cursor.scroll(2)   # 相对移动，从当前位置向后移动2个记录
# result2 = cursor.fetchone()
# print(result2)
#################################
# 修改
# update = "UPDATE departments SET dep_name=%s WHERE dep_name=%s"
# data = ('人力资源部', '人事部')
# cursor.execute(update, data)
#################################
# 删除
delete = "DELETE FROM departments WHERE dep_id=%s"
dep = (6,)
cursor.execute(delete, dep)



#################################
conn.commit()
cursor.close()
conn.close()
