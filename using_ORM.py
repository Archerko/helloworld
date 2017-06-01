#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_ORM.py
from sqlalchemy import Column, create_engine, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:xxzx62100@localhost:3306/arc')

DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id=5, name='NowA')
session.add(new_user)
# 提交即保存到数据库
session.commit()
session.close()

session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id == '5').one()
print 'Type:%s' % type(user)
print 'name:%s' % user.name
session.close()

