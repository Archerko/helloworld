import hashlib


mix = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0',\
     '1','2','3','4','5','6','7','8','9']
mix2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

mix = [x1+x2+x3+x4 for x1 in mix2 for x2 in mix2 for x3 in mix2 for x4 in mix2]
print len(mix)

fourlist=[]
for f1 in mix2:
    for f2 in mix2:
        for f3 in mix2:
            for f4 in mix2:
                fourlist.append(f1+f2+f3+f4)
print len(fourlist)

for src in fourlist:
    m1 = hashlib.md5()
    m1.update(src)
    m2=m1.hexdigest()
    if m2.startswith('6738'):
        print m2
        print src

