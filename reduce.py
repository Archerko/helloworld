# -*- coding:utf-8 -*-
# Filename:reduce.py

a = [1, 2, 3, 5, 8, 9]


def pl(x, y):
    return x*y


def prod(li):
    return reduce(pl, li)
print prod(a)


def fn(m, n):
    return 10 * m + n
print reduce(fn, a)   # 将单独数字组成大整数的方法



