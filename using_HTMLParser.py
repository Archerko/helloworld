#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_HTMLParser.py
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

list1 = list()


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print attrs
        for i in attrs:
            x, y = i
            list1.append(y)
        print '<%s>' % tag

    def handle_endtag(self, tag):
        print '</%s>' % tag

    def handle_startendtag(self, tag, attrs):
        print '<%s/>' % tag

    def handle_data(self, data):
        if 'tor' in data:
            print data
        elif 'Som' in data:
            print data
        else:
            print 'data'

    def handle_comment(self, data):
        print '<!-- -->'

    def handle_charref(self, name):
        print '&#%s;' % name

    def handle_entityref(self, name):
        print '&%s;' % name

parser = MyHTMLParser()
parser.feed('<html><head></head><body><p>Some <a href="1998/ddhjku/117662m/sjjh.jpg">html</a> <a href="aaaa/bbbb/cccc/sjjdndjdjh.png">tutorial...</a><br>END &nbspsss;</p></body></html>')
print list1
