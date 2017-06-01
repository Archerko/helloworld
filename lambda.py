# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:lambda.py

def make_repeater(n):
    return lambda a: a*n

twice =  make_repeater(2)

print twice('word')
print twice(4)

