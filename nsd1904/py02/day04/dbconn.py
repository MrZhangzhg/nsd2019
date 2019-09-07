# MariaDB [nsd1904]> CREATE DATABASE tedu1904 DEFAULT CHARSET utf8;
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建连接mysql数据库的引擎
engin = create_engine(
    # mysql+pymysql://用户:密码@服务器/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1904?charset=utf8',
    encoding='utf8',
    # echo=True   # 打开debug日志，生产环境不要设置
)
Base = declarative_base()  # 生成实体类的基类
Session = sessionmaker(bind=engin)  # 创建会话类

# 创建实体类
class Departments(Base):
    __tablename__ = 'departments'   # 指定类关联的表
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20))

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

class Salary(Base):
    __tablename__ = 'salary'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)


if __name__ == '__main__':
    # 如果库中没有相应的表则创建，有就不会再创建了
    Base.metadata.create_all(engin)
