#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: arc1.py
import numpy as np

La = 2 * np.cos(np.pi/6.0) * 1.0
Lb = 0.5
ab = -(1.0 * np.cos(np.pi/6.0))*(-(np.sin(np.pi/12.0) * 0.5))+(1.0 + np.sin(np.pi/6.0))*(-(np.cos(np.pi/12.0) * 0.5))
cosab = ab/(La*Lb)
print cosab

angel = np.arccos(cosab)
print angel
angel2 = angel*360/2/np.pi
print angel2
