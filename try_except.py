# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:try_except.py

import sys

try:
    s=raw_input('Enter something-->')
except EOFError:
    print '\nWhy did you do an EOF on me?'
    sys.exit() #exit the program

except:
    print '\nSome error/exception occurred.'
    #here,we are not exiting the program

print 'Done!'