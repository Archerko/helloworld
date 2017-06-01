# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:str_methods.py

name = 'Archerko'

if name.startswith('Arc'):
    print "Yes,the string starts with 'Arc'."

if 'a' in name:
    print "Yes,it contains the string 'a'."
else:
    print "No,it does not contain the string 'a'."

if name.find('che') != -1:    #找che在字符串中的位置，-1表示没找到。
    print "Yes,it contains the string 'che'."
    print name.find('che')

delimiter = '_*_'
mylist = ['Brazil','Russia','India','China']
print delimiter.join(mylist)
