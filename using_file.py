# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:using_file.py

poem = '''　　
    Never give up,
　　Never lose hope.
　　Always have faith,
　　It allows you to cope.
　　Trying times will pass,
　　As they always do.
　　Just have patience,
　　Your dreams will come true.
　　So put on a smile,
　　You'll live through your pain.
　　Know it will pass,
　　  And strength you will gain
'''

f=file('poem.txt','w')  #open for 'w'riting
f.write(poem) #write text to file
f.close()

f=file('poem.txt')
while True:
    line =  f.readline()
    if len(line) == 0:
        break
    print line,
f.close()

