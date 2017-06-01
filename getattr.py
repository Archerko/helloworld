# -*- coding: utf-8 -*-
# Filename:__getattr.py


class Ten(object):
    def __init__(self):
        self.name = 'Arc'

    def __getattr__(self, item):
        if item == 'age':
            # return lambda: 32 # 返回函数亦可，但是最后调用注意需要加()
            return 32
        else:
            raise AttributeError("\'Student\' object has no attribute \'%s\'" % item)

a = Ten()

print a.name

print a.age
# print a.age()


