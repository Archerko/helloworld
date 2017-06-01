#coding:utf-8
#!/c:/python27
#Filename:continue.py

while True:
    s=raw_input('You can input something:')
    if s=='quit':
        break
    if len(s) < 5:
        continue
    print 'Your input is',s
    print 'The length of the string is ',len(s)
print 'Done!'
