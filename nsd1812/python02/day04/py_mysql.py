import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1812',
    charset='utf8'
)

cursor = conn.cursor()

create_dep = '''
'''
create_emp = '''
'''
create_sal = '''
'''

cursor.execute(create_dep)
cursor.execute(create_emp)
cursor.execute(create_sal)
conn.commit()

cursor.close()
conn.close()
