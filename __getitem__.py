# -*- coding: utf-8 -*-
# Filename:__getitem__.py


class Fib(object):
    def __getitem__(self, item):
        if isinstance(item,int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item,slice):
            start = item.start
            stop = item.stop
            a, b = 1, 1
            l = []
            for x in range(stop):
                if x >= start:
                    l.append(a)
                a, b = b, a + b
            return l

f = Fib()


print f[10]
print f[2:5]

