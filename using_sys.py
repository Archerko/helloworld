# coding:utf-8
# !/c:/Python27
# Filename:using_sys.py

import sys

print 'The command line arguments are:'
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is',sys.path,'\n'
