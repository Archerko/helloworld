#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_struct.py
import struct

struct.pack('>I', 1034944)

print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
