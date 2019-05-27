#!/opt/djenv/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////var/ftp/nsd_2018/nsd1811/devweb/ansible_project/myansible/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), nullable=False, unique=True)

class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(100), nullable=False, unique=True)
    ipaddr = Column(String(15), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey('webansi_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(HostGroup.groupname, Host.ipaddr).join(Host)
    # print(qset.all())
    result = {}
    for group, ip in qset:
        if group not in result:  # 组不是字典的key，创建一个项目
            result[group] = {}   # result['dbservers'] = {}
            result[group]['hosts'] = [] # result['dbservers']['hosts'] = []
        result[group]['hosts'].append(ip)
    print(json.dumps(result))
