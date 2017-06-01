#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_MySQL.py
import mysql.connector
# 连接数据库，use_unicode=True使MySQL的DB-API始终返回unicode
conn = mysql.connector.connect(user='root', password='xxxxxx', database='arc', use_unicode=True)
# 建立游标来使用SQL操作
cursor = conn.cursor()
# SQL操作数据库
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user (id, name) values (%s, %s)', ['2', 'Bob'])   # MySQL的占位符是%s
# 返回影响的行数
print cursor.rowcount
# 提交数据库进行操作
conn.commit()
# 关闭cursor
cursor.close()
# 再开一个cursor
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('2',))
# fetchall返回所有行
values = cursor.fetchall()
print values
# 关闭cursor和conn
cursor.close()
conn.close()
