#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: cuowujiexian.py

from matplotlib import pyplot as plt
import numpy as np

r1 = np.arange(0, 1.1, 0.1)
x1 = r1 * 0
plt.plot(x1, r1)
plt.text(-0.05, 1.05, 'Ua')

r2 = np.arange(0, 1.1, 0.1)
x2 = r2 * np.cos(np.pi/6.0)
y2 = - r2 * np.sin(np.pi/6.0)
plt.plot(x2, y2)
plt.text(0.88, -0.55, 'Ub')

r3 = np.arange(0, 1.1, 0.1)
x3 = - r3 * np.cos(np.pi/6.0)
y3 = - r3 * np.sin(np.pi/6.0)
plt.plot(x3, y3)
plt.text(-0.98, -0.55, 'Uc')

dianya = 'abc'
dianliu1 = 'Ia'
dianliu2 = 'Ic'
yuanjian1 = ('Uab', dianliu1)
yuanjian2 = ('Ucb', dianliu2)
uabxmax = 1.0 * np.cos(np.pi/6.0)
uabymax = - 1.0 * np.sin(np.pi/6.0)
uabx = np.arange(0, -0.1-uabxmax, -0.1)
uabx[-1] = -uabxmax
uaby = -np.tan(np.pi/3.0) * uabx
plt.plot(uabx, uaby)
plt.text(-0.75, 1.43, 'Uab')

ucbxmax = np.cos(np.pi/6.0) * 1.0
ucbx = np.arange(0, -2*ucbxmax-0.1, -0.1)
ucbx[-1] = -2*ucbxmax
ucby = ucbx * 0
plt.plot(ucbx, ucby)
plt.text(-1.67, 0.05, 'Ucb')

ria = 1.0
iaxmax = np.sin(np.pi/12.0) * ria
iaymax = np.cos(np.pi/12.0) * ria
iax = np.arange(0, iaxmax+0.1, 0.1)
iax[-1] = iaxmax
iay = np.tan(np.pi*(5/12.0)) * iax
plt.plot(iax, iay)
plt.text(0.28, 0.97, 'Ia')

ric = 1.0
icxmax = np.cos(np.pi/12.0) * ric
icx = np.arange(0, -icxmax-0.1, -0.1)
icx[-1] = -icxmax
icy = np.tan(np.pi/12.0) * icx
plt.plot(icx, icy)
plt.text(-1.07, -0.30, 'Ic')


plt.text(-0.17, 0.33, u'30°')
plt.text(0.01, 0.33, u'φ')
plt.text(-0.38, -0.16, u'φ')
plt.text(-1.77, 1.28, u'P1:UIcos(30+φ)')
plt.text(-1.77, 1.08, u'P2:UIcos(330+φ)')
plt.show()
