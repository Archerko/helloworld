# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:html.py

print 'Simple Assignment'

shoplist=['apple','mango','banana','carrot']
mylist=shoplist

del shoplist[0]

print 'shoplist is',shoplist
print 'mylist is',mylist

print 'Copy by making a full silce'
mylist=shoplist[:]
del mylist[0]

print 'shoplist is',shoplist
print 'mylist is',mylist
