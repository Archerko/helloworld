# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:inherit.py

class SchoolMember:
    '''Represents any school member.'''

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print '(Initialized SchoolMember:%s)'%self.name

    def tell(self):
        print "Name:'%s' Age:'%s'"%(self.name,self.age)


class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary=salary
        print '(Initialized Teacher:%s)'%self.name

    def tell(self):
        SchoolMember.tell(self)
        print "Salary:'%s'"%self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks=marks
        print '(Initialized Student:%s)'%self.name

    def tell(self):
        SchoolMember.tell(self)
        print "Marks:'%s'"%self.marks

t = Teacher('Arc',30,50000)
s = Student('Wong',17,100)

print

members = [t,s]
for member in members:
    member.tell()


