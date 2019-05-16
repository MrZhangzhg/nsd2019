from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    # mysql+pymymysql://用户名:密码@服务器/数据库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1812?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上输出日志，生产环境中不要使用
)
# 创建ORM的基类
Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'  # 定义库中的表名
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(50), unique=True, nullable=False)

class Employee(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))



if __name__ == '__main__':
    # 如果库中没有相关的表则创建，有的话不会创建
    Base.metadata.create_all(engine)

