# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:pickling.py

import cPickle as p
#import pickle as p

shoplistfile='shoplist.data'

shoplist=['apple','mango','banana']

f=file(shoplistfile,'w')
p.dump(shoplist,f)
f.close()

f=file(shoplistfile)
storedlist=p.load(f)
print storedlist
print len(storedlist)

