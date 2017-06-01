# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:filter.py


def is_odd(x):
    return x % 2 == 1

print is_odd(3)


def not_ss(s):
    if s == 1:
        return True
    for i in range(2, s):
        if s % i == 0:
            return True
    return False


def filter_ss(n):
    return filter(not_ss, range(1, n+1))

print filter_ss(100)
