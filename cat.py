# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:cat.py

import sys


def readline(filename):
    f=file(filename)
    while True:
        if len(f.readline()) == 0:
            break
        print f.readline()
    f.close()

if len(sys.argv)<2:
    print 'No action specified'
    sys.exit()

if sys.argv[1].startswith('--'): #It's startswith,Not startwith,be carful the 's'.
    option = sys.argv[1][2:]
    if option == 'version':
        print 'Version: 1.2'
    elif option == 'help':
        print '''\
        This program prints files to the standard output.
        Options include:
        --version:Print the version number
        --help:Display this help'''
    else:
        print 'Unknown option.'
else:
    for filename in sys.argv[1:]:
        readline(filename)  #it is a file,not a string.
