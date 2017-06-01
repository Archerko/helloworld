# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:class_init.py

class Person():
    def __init__(self,name):
        self.name = name
    def say_hi(self):
        print 'Hello,my name is',self.name

p = Person('Arc')
p.say_hi()

#It also can be written as Person('Arc').say_hi()
