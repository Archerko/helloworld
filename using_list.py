# coding:utf-8
# !/c:/Python27
# Filename:using_list.py


#This is my shopping list.
shoplist = ['apple','pine','mango','carrot','banana']

print 'I have',len(shoplist),'items to purchase.'

print 'These items are:', #注意尾巴上的逗号
for item in shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now',shoplist

print 'I will sort my list now'
shoplist.sort()
print 'sorted shopping list is',shoplist

print 'The first item i will buy is',shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the',olditem
print 'Now,my shopping list is',shoplist
