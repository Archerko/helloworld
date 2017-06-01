# -*-  coding:utf-8  -*-
# Filename:return_function.py


def lazy_sum(*args):
    def sums():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sums   # 注意这里没有括号，返回的是函数本身，不是调用后的函数

f1 = lazy_sum(2, 3, 4, 5, 7)
f2 = lazy_sum(2, 3, 4, 5, 7)

print f1()
print f2()
print f1
print f2
print f1 == f2
print f1() == f2()


