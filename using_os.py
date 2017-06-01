# -*- coding: utf-8 -*-
# Filename:using_os.py

import os

print os.name
print os.environ
print os.getenv('path')
print os.path.abspath('.')

print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']


def search(s):
    a = [p for p in os.listdir('.') if os.path.isfile(p) and s in p]  # p.find(s) != -1
    b = [p2 for p2 in os.listdir('.') if os.path.isdir(p2)]
    print a
    print b
    for sp in a:
        print sp + '-->' + os.path.abspath(sp)

search('ver')
