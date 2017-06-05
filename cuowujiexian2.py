#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: cuowujiexian2.py
from matplotlib import pyplot as plt
import numpy as np
import math


class CuoWuJieXian(object):
    def __init__(self, uabc, i1, i2):
        self.uabc = uabc
        self.i1 = i1
        self.i2 = i2
        _u_list = list(self.uabc)
        self.u1 = 'U' + _u_list[0] + _u_list[1]
        self.u2 = 'U' + _u_list[2] + _u_list[1]
        self.yj1 = (self.u1, self.i1)
        self.yj2 = (self.u2, self.i2)

        self.x1 = 0     # 第一元件求向量夹角的向量1(U12)的x
        self.x2 = 0     # 第一元件求向量夹角的向量2(I1)的x
        self.y1 = 0     # 第一元件求向量夹角的向量1(U12)的y
        self.y2 = 0     # 第一元件求向量夹角的向量2(I1)y

        self.x3 = 0     # 第二元件求向量夹角的向量1(U32)的x
        self.x4 = 0     # 第二元件求向量夹角的向量2(I2)的x
        self.y3 = 0     # 第二元件求向量夹角的向量1(U32)的y
        self.y4 = 0     # 第二元件求向量夹角的向量2(I2)的y

        self.k = 0      # 实例的k

    def umax(self, u, uno):
        if u == 'Uab':
            uabxmax = -(1.0 * math.cos(np.pi/6.0))
            uabymax = 1.0 + math.sin(np.pi/6.0)
            plt.plot([0, uabxmax], [0, uabymax])
            plt.text(-0.75, 1.43, u+uno)
            plt.text(-0.22, 0.45, u'30°')
            if u == self.u1:
                self.x1 = uabxmax
                self.y1 = uabymax
            elif u == self.u2:
                self.x3 = uabxmax
                self.y3 = uabymax
        elif u == 'Ucb':
            ucbxmax = - 2 * math.cos(np.pi/6.0) * 1.0
            plt.plot([0, ucbxmax], [0, 0])
            plt.text(-1.67, 0.05, u+uno)
            if u == self.u1:
                self.x1 = ucbxmax
                self.y1 = 0
            elif u == self.u2:
                self.x3 = ucbxmax
                self.y3 = 0
        elif u == 'Ubc':
            ubcxmax = 2 * math.cos(np.pi/6.0) * 1.0
            plt.plot([0, ubcxmax], [0, 0])
            plt.text(1.55, 0.06, u+uno)
            if u == self.u1:
                self.x1 = ubcxmax
                self.y1 = 0
            elif u == self.u2:
                self.x3 = ubcxmax
                self.y3 = 0
        elif u == 'Uac':
            uacxmax = 1.0 * math.cos(np.pi/6.0)
            uacymax = 1.0 + math.sin(np.pi/6.0)
            plt.plot([0, uacxmax], [0, uacymax])
            plt.text(0.95, 1.38, u+uno)
            if u == self.u1:
                self.x1 = uacxmax
                self.y1 = uacymax
            elif u == self.u2:
                self.x3 = uacxmax
                self.y3 = uacymax
        elif u == 'Uca':
            ucaxmax = -(1.0 * math.cos(np.pi/6.0))
            ucaymax = -(1.0 + math.sin(np.pi/6.0))
            plt.plot([0, ucaxmax], [0, ucaymax])
            plt.text(-0.72, -1.45, u+uno)
            if u == self.u1:
                self.x1 = ucaxmax
                self.y1 = ucaymax
            elif u == self.u2:
                self.x3 = ucaxmax
                self.y3 = ucaymax
        elif u == 'Uba':
            ubaxmax = 1.0 * math.cos(np.pi/6.0)
            ubaymax = -(1.0 + math.sin(np.pi/6.0))
            plt.plot([0, ubaxmax], [0, ubaymax])
            plt.text(0.93, -1.45, u+uno)
            if u == self.u1:
                self.x1 = ubaxmax
                self.y1 = ubaymax
            elif u == self.u2:
                self.x3 = ubaxmax
                self.y3 = ubaymax
        else:
            print u
            raise ValueError('您输入的电压顺序不正确，请核实后再输入！')

    def imax(self, i, ino):
        if i == 'Ia':
            ria = 0.5
            iaxmax = math.sin(np.pi/12.0) * ria
            iaymax = math.cos(np.pi/12.0) * ria
            plt.plot([0, iaxmax], [0, iaymax])
            plt.text(0.10, 0.62, i+ino)
            plt.text(0.01, 0.33, u'φ')
            if i == self.i1:
                self.x2 = iaxmax
                self.y2 = iaymax
            elif i == self.i2:
                self.x4 = iaxmax
                self.y4 = iaymax
        elif i == 'Ic':
            ric = 0.5
            icxmax = -(math.cos(np.pi/12.0) * ric)
            icymax = -(math.sin(np.pi/12.0) * ric)
            plt.plot([0, icxmax], [0, icymax])
            plt.text(-0.80, -0.18, i+ino)
            plt.text(-0.38, -0.16, u'φ')
            if i == self.i1:
                self.x2 = icxmax
                self.y2 = icymax
            elif i == self.i2:
                self.x4 = icxmax
                self.y4 = icymax
        elif i == '-Ia':
            ria = 0.5
            iaxmax = -(math.sin(np.pi/12.0) * ria)
            iaymax = -(math.cos(np.pi/12.0) * ria)
            plt.plot([0, iaxmax], [0, iaymax])
            plt.text(-0.17, -0.62, i+ino)
            plt.text(-0.07, -0.37, u'φ')
            if i == self.i1:
                self.x2 = iaxmax
                self.y2 = iaymax
            elif i == self.i2:
                self.x4 = iaxmax
                self.y4 = iaymax
        elif i == '-Ic':
            ric = 0.5
            icxmax = math.cos(np.pi/12.0) * ric
            icymax = math.sin(np.pi/12.0) * ric
            plt.plot([0, icxmax], [0, icymax])
            plt.text(0.58, 0.20, i+ino)

            r3a = 1.0   # Uc的反向延长线
            x3a = r3a * math.cos(np.pi/6.0)
            y3a = r3a * math.sin(np.pi/6.0)
            plt.plot([0, x3a], [0, y3a], ':', color='g')
            plt.text(0.30, 0.12, u'φ')

            if i == self.i1:
                self.x2 = icxmax
                self.y2 = icymax
            elif i == self.i2:
                self.x4 = icxmax
                self.y4 = icymax
        else:
            raise ValueError('您输入的电压顺序不正确，请核实后再输入！(注意大小写)')

    def angle(self):
        unorm = 2 * math.cos(np.pi/6.0) * 1.0   # 模
        inorm = 0.5
        dot_product1 = self.x1 * self.x2 + self.y1 * self.y2   # 点乘
        dot_product2 = self.x3 * self.x4 + self.y3 * self.y4
        cross_product1 = self.x1 * self.y2 - self.x2 * self.y1    # 叉乘
        cross_product2 = self.x3 * self.y4 - self.x4 * self.y3
        cosp1 = dot_product1 / (unorm * inorm)  # 向量夹角公式
        cosp2 = dot_product2 / (unorm * inorm)
        pi_anglep1 = math.acos(cosp1)
        pi_anglep2 = math.acos(cosp2)
        if cross_product1 > 0:  # 如果叉乘大于零，则说明这个向量夹角（向量夹角从定义上永远为锐角）的向量u到向量i为逆时针
            anglep1 = 360 - (pi_anglep1 * 180 / np.pi)  # 而实际上要求的角为向量u顺时针到向量i的角，所以用2π-向量夹角
        else:
            anglep1 = pi_anglep1 * 180 / np.pi
        if cross_product2 > 0:
            anglep2 = 360 - (pi_anglep2 * 180 / np.pi)
        else:
            anglep2 = pi_anglep2 * 180 / np.pi
        anglep1_nophi = anglep1 - 15
        anglep2_nophi = anglep2 - 15
        return anglep1_nophi, anglep2_nophi

    def cosphi(self, anglep1_nophi, anglep2_nophi):
        pi_angle1 = math.radians(anglep1_nophi)
        pi_angle2 = math.radians(anglep2_nophi)
        real_cospi12 = math.cos(pi_angle1) + math.cos(pi_angle2)    # P1+P2和差角展开前半部分cos
        real_sinpi12 = math.sin(pi_angle1) + math.sin(pi_angle2)    # 后半部分sin
        cospi12 = round(real_cospi12, 2)     # P1+P2和差角展开前半部分cos，保留2位小数
        sinpi12 = round(real_sinpi12, 2)     # 后半部分sin保留2位小叔
        if cospi12 == 0 and sinpi12 != 0:
            # p12 = str(sinpi12) + u'sinφ'
            self.k = str(round((math.sqrt(3)/real_sinpi12), 2)) + u'ctanφ'
        elif sinpi12 == 0 and cospi12 != 0:
            # p12 = str(cospi12) + u'cosφ'
            self.k = str(round((math.sqrt(3)/real_cospi12), 2))
        elif cospi12 == 0 and sinpi12 == 0:
            self.k = '???'
        else:
            if sinpi12 < 0:
                zfh = '+'
            else:
                zfh = '-'
            p12 = '(' + str(cospi12) + u'cosφ' + zfh + str(sinpi12).replace('-', '') + u'sinφ' + ')'
            self.k = u'√3cosφ/' + p12
        return self.k

    def pltpic(self):
        plt.plot([0, 0], [-1.9, 1.9], ':', color='#666666')
        plt.plot([-1.9, 1.9], [0, 0], ':', color='#666666')

        y1 = 1.0
        x1 = 0
        plt.plot([0, x1], [0, y1])
        plt.text(-0.05, 1.05, 'Ua')

        r2 = 1.0
        x2 = r2 * math.cos(np.pi/6.0)
        y2 = - r2 * math.sin(np.pi/6.0)
        plt.plot([0, x2], [0, y2])
        plt.text(0.88, -0.55, 'Ub')

        r3 = 1.0
        x3 = - r3 * math.cos(np.pi/6.0)
        y3 = - r3 * math.sin(np.pi/6.0)
        plt.plot([0, x3], [0, y3])
        plt.text(-1.05, -0.58, 'Uc')

        self.umax(self.u1, '(U12)')
        self.umax(self.u2, '(U32)')
        self.imax(self.i1, '(I1)')
        self.imax(self.i2, '(I2)')
        plt.text(0.35, 1.90, 'P1: ' + self.u1 + '*' + self.i1.replace('-', '') +
                 '*cos(' + str(int(self.angle()[0])) + u'°+φ)')
        plt.text(0.35, 1.76, 'P2: ' + self.u2 + '*' + self.i2.replace('-', '') +
                 '*cos(' + str(int(self.angle()[1])) + u'°+φ)')
        plt.text(0.35, 1.62, 'k = ' + self.cosphi(self.angle()[0], self.angle()[1]))
        plt.show()

if __name__ == '__main__':
    #uuabc = raw_input('请输入电压顺序：（例如 abc, bac, cab等）')
    #ii1 = raw_input('请再输入电流I1的值：（例如Ia，-Ic等，注意大小写）')
    #ii2 = raw_input('请再输入电流I1的值：（例如Ia，-Ic等，注意大小写）')
    #cw1 = CuoWuJieXian(uuabc, ii1, ii2)
    fig = plt.figure(figsize=(7, 7))
    cw1 = CuoWuJieXian('cba', '-Ia', 'Ic')
    cw1.pltpic()



