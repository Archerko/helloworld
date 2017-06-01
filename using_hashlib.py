#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_hashlib.py
import hashlib

md5 = hashlib.md5()
md5.update('cnbeta')
print md5
print md5.hexdigest()
md5 = hashlib.md5()   # 必须新建一个实例,不然update()会在原基础上增加字符串
print md5
md5.update('helloworld')
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('What the fucking??')
print sha1
print sha1.hexdigest()
sha1 = hashlib.sha1()
sha1.update('What the fucking??')
print sha1
print sha1.hexdigest()

sha512 = hashlib.sha512()
sha512.update('What the fucking??')
print sha512.hexdigest()

db = {}


def get_md5(item):
    usermd5 = hashlib.md5()
    usermd5.update(item)
    return usermd5.hexdigest()


def register(username, password):
    db[username] = get_md5(password + username + 'Wtf!@')


def reg():
    username = raw_input('reg username:')
    password = raw_input('reg password:')
    return register(username, password)


def login(username, password):
    if get_md5(password + username + 'Wtf!@') == db[username]:
        print 'True'
        return True
    else:
        print 'False'
        return False


def main():
    username = raw_input('username:')
    password = raw_input('password:')
    return login(username, password)

reg()
main()
