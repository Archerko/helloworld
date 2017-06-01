#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_collections.py
import collections

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y
print p[0]
print isinstance(p, Point)
print isinstance(p, tuple)
print '-------------------------------------------------------------'

q = collections.deque(['a', 'b', 'c'])
q.append(1)
q.appendleft('!')
print q
print q[0]
print '-------------------------------------------------------------'

dd = collections.defaultdict(lambda: 'N/A')  # 返回值是函数
dd['key1'] = 'abc'
print dd['key1']
print dd['key2']  # key2不存在
print '-------------------------------------------------------------'

d = dict([('a', 1), ('b', 2), ('c', 3)])
print d  # dict是无序的
od = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od  # OrderedDict是有序的
# od会按照插入的顺序排序，不是Key值排序
print '-------------------------------------------------------------'

c = collections.Counter()
for ch in 'Programming':
    c[ch] = c[ch] + 1
print c

print collections.Counter('Programming')
