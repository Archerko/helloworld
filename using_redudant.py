# -*- coding: utf-8 -*-
# Filename:using_redudant.py
import re

a = 'bill.gates@hjk.com'

if re.match(r'^([a-z.]+)@(\w{1,20})\.(\w{1,8})', a):
    print 'ok'
else:
    print 'failed'

print re.match(r'^([a-z.]+)@(\w{1,20})\.(\w{1,8})', a).groups()


b = '<Tom Paris> tom@voyager.org'

re_email = re.compile(r'^<(\w+\s\w+)>\s+\w+@\w+\.org|com$')
if re_email.match(b):
    print "ok"

print re_email.match(b).group(0)
print re_email.match(b).group(1)
