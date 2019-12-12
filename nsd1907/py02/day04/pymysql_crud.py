import pymysql

# 创建连接
conn = pymysql.connect(
    user='root',
    port=3306,
    host='127.0.0.1',
    passwd='tedu.cn',
    db='nsd1907',
    charset='utf8'
)

# 创建游标
cur = conn.cursor()

# 创建部门
# insert1 = "INSERT INTO departments VALUES(%s, %s)"
# cur.execute(insert1, (1, '人事部'))
# cur.executemany(insert1, [(2, '运维部'), (3, '开发部'), (4, '测试部')])
# cur.executemany(insert1, ((4, '测试部'), (5, '市场部'), (6, '销售部')))


# 更新部门，将人事部改为人力资源部
# update1 = "UPDATE departments SET dep_name=%s WHERE dep_name=%s"
# cur.execute(update1, ('人力资源部', '人事部'))

# 删除4号部门
# del1 = "DELETE FROM departments WHERE dep_id=%s"
# cur.execute(del1, (4,))

# 查询
select1 = "SELECT * FROM departments"
cur.execute(select1)
result1 = cur.fetchone()  # 取一个记录
print(result1)
print('*' * 30)
result2 = cur.fetchmany(2)  # 继续取出2个记录
print(result2)
print('*' * 30)
result3 = cur.fetchall()  # 取出剩余全部记录
print(result3)


# 确认提交
conn.commit()

# 关闭
cur.close()
conn.close()
