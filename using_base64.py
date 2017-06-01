#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_base64.py
import base64

a = base64.b64encode('What the Fuck \x00string1111')
print a

b = base64.b64decode('V2hhdCB0aGUgRnVjayAAc3RyaW5nMQ==')
print b

c = base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print c

d = base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print d

e = base64.urlsafe_b64decode('abcd--__')
print e


def safe_b64decode(s):
    print len(s)
    if len(s) % 4 == 2:
        s = s + '=='
    elif len(s) % 4 == 3:
        s = s + '='
    else:
        s = s
    print base64.b64decode(s)

safe_b64decode('V2hhdCB0aGUgRnVjayAAc3RyaW5nMTExMQ')
print
