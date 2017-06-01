# -*- coding: utf-8 -*-
# Filename:using_codecs.py
import codecs

with codecs.open('1.txt', 'r', 'utf-8') as p:
    print p.read()

t = open('c:/test/IMG00000.bmp', 'rb')
print t.read()
