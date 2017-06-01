import hashlib


m1 = hashlib.md5()

m1.update('101999966233')
a=m1.hexdigest()
print a



