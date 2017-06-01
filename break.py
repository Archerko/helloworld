#coding:utf-8
#!/c:/python27
#Filename:break.py

while True:
    s=raw_input('You can input something:')
    if s=='quit':
        break
    print 'Your input is',s
    print 'The length of the string is ',len(s)
print 'Done!'
