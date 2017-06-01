#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_itertools.py
import itertools

natuals = itertools.count(1)   # 无限打印自然数列，根本停不下来

cs = itertools.cycle('ABCD')   # 无线循环打印字符串，根本停不下来

ns = itertools.repeat('A', 10)   # 循环指定次数的元素
for i in ns:
    print i

nt = itertools.takewhile(lambda x: x <= 10, natuals)
for i in nt:
    print i

for c in itertools.chain('ABD', 'HHH'):
    print c

for key, group in itertools.groupby('AAAVVVDDD'):
    print key, list(group)

for key, group in itertools.groupby('AAaaBbbBbbcCCC', lambda x: x.lower()):
    print key, list(group)

for a in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print a

r = itertools.imap(lambda x: x*x, itertools.count(1))
for i in itertools.takewhile(lambda x: x <= 100, r):
    print i
