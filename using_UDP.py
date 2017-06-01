#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_UDP.py
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9999))

print 'Bind UDP on 9999...'
while True:
    data, addr = s.recvfrom(1024)
    print addr
    print 'Received from %s:%s' % addr  # addr 是一个tuple ('IP',Port)
    s.sendto('Hello,%s!' % data, addr)
