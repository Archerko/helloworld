# -*- coding: cp936 -*-
import binascii
import struct


# 每个字节转成hex，0x顺便去掉，对于不足两位的补0
def str2hex(str):
    hexs = []
    for s in str:
        tmp = (hex(ord(s)).replace('0x', ''))
        if len(tmp) == 2:
            hexs.append(tmp)
        else:
            hexs.append('0' + tmp)
    return hexs


arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
arr2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def tran(r):
    for i in range(len(arr)):
        if r == arr[i]:
            return arr2[i]


f = open('1.txt', 'rb')
f2 = open('2.txt', 'rb')
hexs = []
hexs2 = []
while True:
    t = f.readline()
    t2 = f2.readline()
    if not t or not t2:
        break
    hexs.extend(str2hex(t))
    hexs2.extend(str2hex(t2))
f.close()
f2.close()

ff = open('out.txt', 'wb')
for i in range(min(len(hexs), len(hexs2))):
    a = tran(hexs[i][0]) * 16 + tran(hexs[i][1])
    b = tran(hexs2[i][0]) * 16 + tran(hexs2[i][1])
    B = struct.pack('B', a ^ b)
    ff.write(B)
ff.close()