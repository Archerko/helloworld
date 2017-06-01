# -*- coding: utf-8 -*-
# Filename:property.py


class Test(object):
    def __init__(self, name):
        self.name = name

    def printname(self):
        print self.name

    @property   # 使用property在给 a.score = 100 加输入条件判断的时候，简化a.get_score(100)写法为a.score = 100
    def score(self):
        return self._score

    @score.setter   # property装饰器的目的是将方法变为属性，感觉很屌啊！
    def score(self, sc):
        if not isinstance(sc, int):
            raise ValueError("必须输入数字")
        if sc < 0 or sc > 100:
            raise ValueError('输入的数字必须在0-100之间')
        self._score = sc

a = Test('Arc')
b = Test('Bob')

a.printname()
b.printname()

print hasattr(a, 'name')
print a.name
print getattr(a, 'name')

print hasattr(a, 'age')
setattr(a, 'age', 20)
print hasattr(a, 'age')
print getattr(a, 'age')

a.score = 80
print a.score
