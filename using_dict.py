# coding:utf-8
# !/c:/Python27
# Filename:using_dict.py

#'ab' is short for 'addressbook'

ab = {'Arc':'arc@qq.com',
      'Bob':'Bob@qq.com',
      'Span':'Spanin@qq.com',
      'Alex':'Alex520@163.com'

}

print "Arc's address is %s" %ab['Arc']

#Add a key/value pair
ab['Guido']='guido@python.org'

#Deleting a key/value pair
del ab['Span']

print '\nThere are %d contacts in the address-book\n' %len(ab)
for name,address in ab.items():
    print 'Contact %s at %s' %(name,address)

if 'Guido' in ab:         #OR ab.has_key('Guido')
    print "\nGuido's address is %s" %ab['Guido']

