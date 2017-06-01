# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:bacon.py

s = raw_input('输入初始字符串-->')

print s.isalpha()

s1 = ''.join([a for a in s if a.isalpha()])
s2 = []
s3 = []
print s1

for i in range(0, len(s1)):
    if s1[i].lower() == s1[i]:
        s2.append('a')
        s3.append('b')
    else:
        s2.append('b')
        s3.append('a')

print s2
print s3

s4=''.join(s2)
s5=''.join(s3)

print s4
print s5

basebacon = 0

s6 = []
s7 = []

for i2 in range(0, len(s4)/5):
    print s4[basebacon:(basebacon+5)]
    s6.append(s4[basebacon:(basebacon+5)])
    basebacon = basebacon + 5

basebacon2 = 0

for i3 in range(0, len(s5)/5):
    print s5[basebacon2:(basebacon2+5)]
    s7.append(s5[basebacon2:(basebacon2+5)])
    basebacon2 = basebacon2 + 5

print s6
print s7

bacon={'aaaaa':'A','aaaab':'B','aaaba':'C','aaabb':'D','aabaa':'E',
'aabab':'F','aabba':'G','aabbb':'H','abaaa':'I','abaab':'J',
'ababa':'K','ababb':'L','abbaa':'M','abbab':'N','abbba':'O',
'abbbb':'P','baaaa':'Q','baaab':'R','baaba':'S','baabb':'T',
'babaa':'U','babab':'V','babba':'W','babbb':'X','bbaaa':'Y',
'bbaab':'Z'
}

print '-------Finally,We Get the Key!--------'

for i4 in range(0, len(s6)):
    if s6[i4] in bacon:
        print bacon[s6[i4]],
    else:
        print '*',

print

for i5 in range(0, len(s7)):
    if s7[i5] in bacon:
        print bacon[s7[i5]],
    else:
        print '*',

print
print '-----↑↑--bacon #1--↑↑-----'

bacon2={'aaaaa':'A','aaaab':'B','aaaba':'C','aaabb':'D','aabaa':'E',
'aabab':'F','aabba':'G','aabbb':'H','abaaa':'I(J)','abaab':'K',
'ababa':'L','ababb':'M','abbaa':'N','abbab':'O','abbba':'P',
'abbbb':'Q','baaaa':'R','baaab':'S','baaba':'T','baabb':'U(V)',
'babaa':'W','babab':'X','babba':'Y','babbb':'Z'
}

for i6 in range(0, len(s6)):
    if s6[i6] in bacon2:
        print bacon2[s6[i6]],
    else:
        print '*',

print

for i7 in range(0, len(s7)):
    if s7[i7] in bacon2:
        print bacon[s7[i7]],
    else:
        print '*',

print '\n-----↑↑--bacon #2--↑↑-----'
