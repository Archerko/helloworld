# -*-  coding:utf-8  -*-
# Filename:decorator.py

import time
import functools


def log(func):
    @functools.wraps(func)
    def wra(*args, **kwargs):
        print 'calling %s()...' % func.__name__
        return func(*args, **kwargs)
    return wra


@log    # now = log(now)
def now():
    print time.strftime('%H:%M:%S')

now()
print now.__name__


def log2(text):
    def deco(func):
        @functools.wraps(func)
        def wra2(*args, **kwargs):
            print 'calling %s %s()...' % (text, func.__name__)
            return func(*args, **kwargs)
        return wra2
    return deco


@log2('the fucking')    # now = log2('the fucking')(now)
def now2(yoyo):
    print yoyo
    print time.strftime('%H:%M:%S')

now2('haha')
print now2.__name__


def log3(func):
    @functools.wraps(func)
    def wr3(*args, **kwargs):
        print 'begin call'
        result = func(*args, **kwargs)    # 直接调用func将导致wr3的返回值为None，导致最后的now3()返回值也为None
        print 'end call'    # 所以用一个变量result将func的值先导出
        return result   # 这里使用变量名可以避免再次调用func函数
    return wr3


@log3
def now3():
    print time.strftime('%H:%M:%S')
    return time.strftime('%H')

print now3()
