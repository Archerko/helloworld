# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:switch_ip.py

import os

print "请输入需要用哪个网络"
print "1、内网（87段）"
print "2、外网（136段）"
print "3、自动获取IP"

switch = raw_input('请在这里输入想要的网段-->')
if switch == '1':
    os.system('netsh interface ip set address TypeC1000M static 192.168.87.205 255.255.255.0')
    os.system('netsh interface ip set dns TypeC1000M static none')
elif switch == '2':
    os.system('netsh interface ip set address TypeC1000M static 192.168.136.202 255.255.252.0 192.168.136.1')
    os.system('netsh interface ip set dns TypeC1000M static 202.103.24.68')
elif switch == '3':
    os.system('netsh interface ip set address TypeCNET dhcp')
    os.system('netsh interface ip set dns TypeCNET dhcp')
else:
    print "输入错误！"





