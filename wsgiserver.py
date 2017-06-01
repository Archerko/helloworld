#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: wsgiserver.py
from wsgiref.simple_server import make_server
from wsgihello import application

httpd = make_server('', 8000, application)
print 'Server HTTP on port 8000...'
httpd.serve_forever()
