# coding:utf-8
# !/c:/Python27
# Filename:func_doc.py

def print_max(x,y):
    '''中文能放前面吗？Print the maximum of two numbers.
    
    The two values must be integers.'''

    x = int(x)
    y = int(y)

    if x>y:
        print x,'is maximum.'
    else:
        print y,'is maximum.'

print_max(7,3)
print print_max.__doc__
