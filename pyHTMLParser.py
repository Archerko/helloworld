#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: pyHTMLParser.py
from HTMLParser import HTMLParser
import urllib


class PythonHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.events = dict()
        self.count = 0
        self.eventdata = None

    def handle_starttag(self, tag, attrs):
        if tag == 'h3' and attrs.__contains__(('class', 'event-title')):
            self.count += 1   # 这里是1
            self.events[self.count] = dict()
            self.eventdata = 'event-title'
        elif tag == 'time':
            self.eventdata = 'time'
        elif tag == 'span' and attrs.__contains__(('class', 'event-location')):
            self.eventdata = 'event-location'

    def handle_data(self, data):
        if self.eventdata == 'event-title':
            self.events[self.count]['event-title'] = data
        elif self.eventdata == 'time':
            self.events[self.count]['time'] = data
        elif self.eventdata == 'event-location':
            self.events[self.count]['event-location'] = data
        self.eventdata = None  # 别忘了这行，不然捕获到的其他内容的标记没清除，会继续执行上面的命令，冲掉实际内容

    def eventslist(self):
        print '这段时间有如下会议：'
        for i in self.events.values():  # values()可以表示整个dict的list
            print '会议名称：%s  会议时间：%s  会议地点：%s' % (i['event-title'], i['time'], i['event-location'])

try:
    parser = PythonHTMLParser()
    pypage = urllib.urlopen('https://www.python.org/events/python-events/')
    pyhtml = pypage.read()
except IOError, e:
    print 'IOError:', e
else:
    parser.feed(pyhtml)
    parser.eventslist()
finally:
    pypage.close()
