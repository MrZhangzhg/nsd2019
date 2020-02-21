from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建引擎，用于指定操作的数据库
engine = create_engine(
    # mysql+pymysql://用户名:密码@服务器/数据库?选项
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1909?charset=utf8',
    encoding='utf8',  # 字符编码
    # echo=True         # 在终端上打印debug日志信息，生产环境下不要打开
)

# 创建会话类，用于连接到数据库，通过会话连接操作数据库
Session = sessionmaker(bind=engine)

# 创建实体类(数据库中表对应的类)的基类
Base = declarative_base()

# 创建实体类
class Department(Base):
    __tablename__ = 'departments'   # 声明该类与哪个表关联
    dep_id = Column(Integer, primary_key=True)  # dep_id字段，整型，主键
    dep_name = Column(String(20), unique=True)  # dep_name字段，VARCHAR(20)，唯一

    def __str__(self):
        return "%s:%s" % (self.dep_name, self.dep_id)

class Employee(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20))
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
    # 创建表，如果表已存在，不会报错，不会重建
    Base.metadata.create_all(engine)
