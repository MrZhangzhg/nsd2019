from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建到mysql数据库的连接引擎
engine = create_engine(
    # mysql+pymysql://用户:密码@主机/库?参数
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1907?charset=utf8',
    encoding='utf8',
    # echo=True  # 在屏幕上打印日志
)

# 创建实体类的基类
Base = declarative_base()

# 创建到数据库连接的会话类
Session = sessionmaker(bind=engine)

# 创建实体类，也就是创建表对应的类
class Departments(Base):
    __tablename__ = 'departments'  # 声明类对应的表
    # 每个字段都要用Column来定义
    dep_id = Column(Integer, primary_key=True)  # 主键
    dep_name = Column(String(20), unique=True)  # 名称必须唯一

    def __str__(self):
        return "部门: %s" % self.dep_name

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
    # 如果库中无表则创建，有表将不会执行
    Base.metadata.create_all(engine)
