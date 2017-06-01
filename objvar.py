# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:objvar.py

class Person():
    '''Represents a person.'''
    population = 0

    def __init__(self,name):
        '''Initializes the person's data.'''
        self.name = name
        print '(Initializing %s)' %self.name

        Person.population += 1


    def __del__(self):
        '''I am dying.'''
        print '%s say goodbye.' %self.name

        Person.population -= 1

        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %s people left.' %Person.population

    def say_hi(self):
        '''Greeting by the person.
        
        Really,that's all it does.'''
        print 'Hi,I am %s'%self.name

    def how_many(self):
        if Person.population == 1:
            print 'I am the only person here'
        else:
            print 'We have %s persons here.'%Person.population

swaroop = Person('Swaroop')
swaroop.say_hi()
swaroop.how_many()

kalam = Person('Abdul Kalam')
kalam.say_hi()
kalam.how_many()

swaroop.say_hi()
swaroop.how_many()

print Person.__doc__
print Person.say_hi.__doc__