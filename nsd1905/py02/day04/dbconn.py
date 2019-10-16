from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建到数据库的引擎
engine = create_engine(
    # mysql+pymysql://用户:密码@服务器/数据库?选项
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1905?charset=utf8',
    encoding='utf8',
    # echo=True  # 显示调试信息，生产环境下不要设置
)
# 创建连接数据库的会话类
Session = sessionmaker(bind=engine)

# 生成实体类的基类
Base = declarative_base()

class Departments(Base):
    __tablename__ = 'departments'  # 指定类对应的表
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True)

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
    # 如果库中没有表则创建，有的话只是进行关联，不会再创建一遍
    Base.metadata.create_all(engine)
