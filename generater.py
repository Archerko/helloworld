# -*- coding:utf-8 -*-
# Filename:generater.py


def add():
    print 'Step 1:'
    yield 1
    print 'Step 2:'
    yield 3
    print 'Step 3:'
    yield 5

o = add()
print o.next()
print o.next()  # generater里，yield相当于return，在非交互环境中，获得的值不会显示出来的。
print o.next()

