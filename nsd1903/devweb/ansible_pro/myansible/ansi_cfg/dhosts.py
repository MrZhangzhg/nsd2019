#!/root/nsd1903/bin/python

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////var/ftp/nsd2019/nsd1903/devweb/ansible_pro/myansible/db.sqlite3',
    encoding='utf8',
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Group(Base):
    __tablename__ = 'webadmin_group'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True)

class Host(Base):
    __tablename__ = 'webadmin_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webadmin_group.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(Group.groupname, Host.ipaddr).join(Host)
    # print(qset.all())
    # [('dbservers', '192.168.4.5'), ('webservers', '192.168.4.7'), ('webservers', '192.168.4.6')]
    result = {}
    for g, ip in qset:
        if g not in result:
            result[g] = {}  # {'dbservers': {}}
            result[g]['hosts'] = []  # {'dbservers': {'hosts': []}}
        result[g]['hosts'].append(ip)
    print(json.dumps(result))
