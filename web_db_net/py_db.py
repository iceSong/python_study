# -*- coding:utf-8 -*-
# SQLite python中内置了sqlite3
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('drop TABLE IF EXISTS user')
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user(`id`, `name`) values(\'1\', \'Michael\')')
print(cursor.rowcount)
cursor.close()
conn.close()

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('insert into user(`id`, `name`) values(\'2\', \'Michael\')')
cursor.execute('select * from user')
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()


# 使用mysql
import mysql.connector

# 使用orm框架
# 安装sqlalchemy   pip3 install sqlalchemy
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象基类
Base = declarative_base()


# 定义User对象
class User(Base):
    __tablename__ = 'user'

    # 表结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接
engine = create_engine('mysql+mysqlconnector://dev:dev@121.42.143.168:3306/test')  # 初始化数据库连接池
# 数据库类型+数据库驱动器名：//用户名:口令@机器地址：端口号/数据库名
DBSession = sessionmaker(bind=engine)

# orm插入数据
session = DBSession()
new_user = User(id='5', name='Bob')
session.add(new_user)
session.commit()
session.close()

# orm获取数据
session1 = DBSession()
user = session1.query(User).filter(User.id=='5').one()
print('type:', type(user))
print('name:', user.name)
