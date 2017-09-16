#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: cuowujiexian2.py
from matplotlib import pyplot as plt
import numpy as np
import math
import Tkinter
import tkFont
import tkMessageBox
import re

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

        self.umax_init(self.u1)     # 必须将这四个函数放到init里来，不然self.x1之类的参数初始化后为0，会引起错误
        self.umax_init(self.u2)
        self.imax_init(self.i1)
        self.imax_init(self.i2)

    def umax_init(self, u):
        if u == 'Uab':
            uabxmax = -(1.0 * math.cos(np.pi/6.0))
            uabymax = 1.0 + math.sin(np.pi/6.0)
            if u == self.u1:
                self.x1 = uabxmax
                self.y1 = uabymax
            elif u == self.u2:
                self.x3 = uabxmax
                self.y3 = uabymax
        elif u == 'Ucb':
            ucbxmax = - 2 * math.cos(np.pi/6.0) * 1.0
            if u == self.u1:
                self.x1 = ucbxmax
                self.y1 = 0
            elif u == self.u2:
                self.x3 = ucbxmax
                self.y3 = 0
        elif u == 'Ubc':
            ubcxmax = 2 * math.cos(np.pi/6.0) * 1.0
            if u == self.u1:
                self.x1 = ubcxmax
                self.y1 = 0
            elif u == self.u2:
                self.x3 = ubcxmax
                self.y3 = 0
        elif u == 'Uac':
            uacxmax = 1.0 * math.cos(np.pi/6.0)
            uacymax = 1.0 + math.sin(np.pi/6.0)
            if u == self.u1:
                self.x1 = uacxmax
                self.y1 = uacymax
            elif u == self.u2:
                self.x3 = uacxmax
                self.y3 = uacymax
        elif u == 'Uca':
            ucaxmax = -(1.0 * math.cos(np.pi/6.0))
            ucaymax = -(1.0 + math.sin(np.pi/6.0))
            if u == self.u1:
                self.x1 = ucaxmax
                self.y1 = ucaymax
            elif u == self.u2:
                self.x3 = ucaxmax
                self.y3 = ucaymax
        elif u == 'Uba':
            ubaxmax = 1.0 * math.cos(np.pi/6.0)
            ubaymax = -(1.0 + math.sin(np.pi/6.0))
            if u == self.u1:
                self.x1 = ubaxmax
                self.y1 = ubaymax
            elif u == self.u2:
                self.x3 = ubaxmax
                self.y3 = ubaymax
        else:
            print u
            raise ValueError('您输入的电压顺序不正确，请核实后再输入！')

    def imax_init(self, i):
        if i == 'Ia':
            ria = 0.5
            iaxmax = math.sin(np.pi/12.0) * ria
            iaymax = math.cos(np.pi/12.0) * ria
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

            if i == self.i1:
                self.x2 = icxmax
                self.y2 = icymax
            elif i == self.i2:
                self.x4 = icxmax
                self.y4 = icymax
        else:
            raise ValueError('您输入的电压顺序不正确，请核实后再输入！(注意大小写)')

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
        cospi12 = round(real_cospi12, 3)     # P1+P2和差角展开前半部分cos，保留2位小数
        sinpi12 = round(real_sinpi12, 3)     # 后半部分sin保留2位小叔
        if cospi12 == 0 and sinpi12 != 0:
            # p12 = str(sinpi12) + u'sinφ'
            if sinpi12 < 0:
                self.k = str(round((math.sqrt(3)/real_sinpi12), 3)).replace('-', '') + u'cotφ'
            else:
                self.k = '-' + str(round((math.sqrt(3)/real_sinpi12), 3)).replace('-', '') + u'cotφ'
        elif sinpi12 == 0 and cospi12 != 0:
            # p12 = str(cospi12) + u'cosφ'
            self.k = str(round((math.sqrt(3)/real_cospi12), 3))
        elif cospi12 == 0 and sinpi12 == 0:
            self.k = u'∞'
        else:
            if sinpi12 < 0:
                zfh = '+'   # cos(a+b)展开的中间有负号，做个判断
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

        plt.text(0.30, 1.90, 'P1: ' + self.u1 + '*' + self.i1.replace('-', '') +
                 '*cos(' + str(int(self.angle()[0])) + u'°+φ)')
        plt.text(0.30, 1.76, 'P2: ' + self.u2 + '*' + self.i2.replace('-', '') +
                 '*cos(' + str(int(self.angle()[1])) + u'°+φ)')
        plt.text(0.30, 1.62, u'k = ' + self.cosphi(self.angle()[0], self.angle()[1]))
        plt.show()

    @staticmethod
    def real_k(anglep1_nophi, anglep2_nophi, phi, sinphi, cosphi):
        if phi == 0:
            _sinphi = sinphi
            _cosphi = cosphi
        else:
            _phi = math.radians(phi)
            _sinphi = math.sin(_phi)
            _cosphi = math.cos(_phi)
        pi_angle1 = math.radians(anglep1_nophi)
        pi_angle2 = math.radians(anglep2_nophi)
        real_cospi12 = math.cos(pi_angle1) + math.cos(pi_angle2)    # P1+P2和差角展开前半部分cos
        real_sinpi12 = math.sin(pi_angle1) + math.sin(pi_angle2)    # 后半部分sin
        if round(real_cospi12, 5) == 0 and round(real_sinpi12, 5) != 0:
            k = -math.sqrt(3)/real_sinpi12 * (_cosphi/_sinphi)
            k = round(k, 4)
        elif round(real_sinpi12, 5) == 0 and round(real_cospi12, 5) != 0:
            k = math.sqrt(3)/real_cospi12
            k = round(k, 4)
        elif round(real_cospi12, 5) == 0 and round(real_sinpi12, 5) == 0:
            k = u'∞'
        else:
            p12 = real_cospi12 * _cosphi - real_sinpi12 * _sinphi
            if round(p12, 3) == 0:
                k = u'∞'
            else:
                k = (math.sqrt(3) * _cosphi) / p12
                k = round(k, 4)
        return k


class CWJXGUI(Tkinter.Frame):
    uabclist = ['abc', 'bca', 'cab', 'acb', 'bac', 'cba']
    ilist = ['Ia', 'Ic', '-Ia', '-Ic']

    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        tf20 = tkFont.Font(size=15, family='宋体')
        tf_an = tkFont.Font(size=20, family='黑体')
        self.app_name = Tkinter.Label(self, text='电能计量错误接线判断（基础版ver 0.48）', font=tf_an)
        self.uabc_name = Tkinter.Label(self, text='U', font=tf20)
        self.ii1_name = Tkinter.Label(self, text='I1', font=tf20)
        self.ii2_name = Tkinter.Label(self, text='I2', font=tf20)
        self.xuanding = Tkinter.Label(self, text='选定：', font=tf20, fg='red')
        self.uabc_xd = Tkinter.Label(self, text='U', font=tf20)
        self.ii1_xd = Tkinter.Label(self, text='I1', font=tf20)
        self.ii2_xd = Tkinter.Label(self, text='I2', font=tf20)
        self.uabc_listbox = Tkinter.Listbox(self, height=8, width=6, font=tf20)
        self.ii1_listbox = Tkinter.Listbox(self, height=8, width=6, font=tf20)
        self.ii2_listbox = Tkinter.Listbox(self, height=8, width=6, font=tf20)
        self.uabc_button = Tkinter.Button(self, text='↓↓↓', command=self.uabc_func)
        self.uabcvar = Tkinter.StringVar()
        self.uabc_chose = Tkinter.Entry(self, textvariable=self.uabcvar, width=6, font=tf20, state='readonly')
        self.ii1_button = Tkinter.Button(self, text='↓↓↓', command=self.ii1_func)
        self.ii1var = Tkinter.StringVar()
        self.ii1_chose = Tkinter.Entry(self, textvariable=self.ii1var, width=6, font=tf20, state='readonly')
        self.ii2_button = Tkinter.Button(self, text='↓↓↓', command=self.ii2_func)
        self.ii2var = Tkinter.StringVar()
        self.ii2_chose = Tkinter.Entry(self, textvariable=self.ii2var, width=6, font=tf20, state='readonly')
        self.refresh_button = Tkinter.Button(self, text='生成\n图形', font=tf20, command=self.refresh_func)

        self.p1_name = Tkinter.Label(self, text='第一元件：', font=tf20)
        self.p1_name_u = Tkinter.Label(self, text='U12', width=5, font=tf20)
        self.p1_u_var = Tkinter.StringVar()
        self.p1_u = Tkinter.Entry(self, textvariable=self.p1_u_var, width=6, font=tf20, state='readonly')
        self.p1_name_i1 = Tkinter.Label(self, text='I1', width=5, font=tf20)
        self.p1_i1_var = Tkinter.StringVar()
        self.p1_i1 = Tkinter.Entry(self, textvariable=self.p1_i1_var, width=6, font=tf20, state='readonly')
        self.p1_i1_blank = Tkinter.Label(self, width=16, font=tf20)
        self.p1_name_p = Tkinter.Label(self, text='P1', width=5, font=tf20)
        self.p1_p_var = Tkinter.StringVar()
        self.p1_p = Tkinter.Entry(self, textvariable=self.p1_p_var, font=tf20, width=35, state='readonly')

        self.p2_name = Tkinter.Label(self, text='第二元件：', font=tf20)
        self.p2_name_u = Tkinter.Label(self, text='U32', width=5, font=tf20)
        self.p2_u_var = Tkinter.StringVar()
        self.p2_u = Tkinter.Entry(self, textvariable=self.p2_u_var, width=6, font=tf20, state='readonly')
        self.p2_name_i2 = Tkinter.Label(self, text='I2', width=5, font=tf20)
        self.p2_i2_var = Tkinter.StringVar()
        self.p2_i2 = Tkinter.Entry(self, textvariable=self.p2_i2_var, width=6, font=tf20, state='readonly')
        self.p2_i2_blank = Tkinter.Label(self, width=16, font=tf20)
        self.p2_name_p = Tkinter.Label(self, text='P2', width=5, font=tf20)
        self.p2_p_var = Tkinter.StringVar()
        self.p2_p = Tkinter.Entry(self, textvariable=self.p2_p_var, font=tf20, width=35, state='readonly')

        self.k_name = Tkinter.Label(self, text='退补率：', font=tf20)
        self.k_name_k = Tkinter.Label(self, text='k', font=tf20)
        self.k_var = Tkinter.StringVar()
        self.k_k = Tkinter.Entry(self, textvariable=self.k_var, width=35, font=tf20, state='readonly')

        self.phi_name = Tkinter.Label(self, text=u'φ的参数：', font=tf20)
        self.phi_name_solo = Tkinter.Label(self, text=u'φ', width=5, font=tf20)
        self.phi_var = Tkinter.StringVar()
        self.phi_solo = Tkinter.Entry(self, width=6, textvariable=self.phi_var, font=tf20)
        self.phi_name_sin = Tkinter.Label(self, text=u'sinφ', width=5, font=tf20)
        self.sinphi_var = Tkinter.StringVar()
        self.phi_sin = Tkinter.Entry(self, textvariable=self.sinphi_var, width=6, font=tf20)
        self.phi_name_cos = Tkinter.Label(self, text=u'cosφ', width=5, font=tf20)
        self.cosphi_var = Tkinter.StringVar()
        self.phi_cos = Tkinter.Entry(self, width=6, textvariable=self.cosphi_var, font=tf20)
        self.phi_blank = Tkinter.Label(self, width=3, font=tf20)

        self.k_button = Tkinter.Button(self, text='计算k值', font=tf20, command=self.k_func)

        self.k_result_name = Tkinter.Label(self, text='退补率值：', font=tf20)
        self.k_result_k = Tkinter.Label(self, text='k', font=tf20)
        self.k_result_var = Tkinter.StringVar()
        self.k_result = Tkinter.Entry(self, width=35, font=tf20, textvariable=self.k_result_var, state='readonly')
        self.k_result_blank = Tkinter.Label(self, width=20, font=tf20)

        self.rightside = Tkinter.Label(self, width=4, font=tf20)
        self.create_widgets()

    def create_widgets(self):
        self.app_name.grid(column=0, row=0, columnspan=16)   # APP标题

        self.xuanding.grid(column=0, row=8, padx=10, pady=3)  # ‘选定’

        self.uabc_name.grid(column=2, row=1, padx=10, pady=3)
        self.ii1_name.grid(column=4, row=1, padx=10, pady=3)
        self.ii2_name.grid(column=6, row=1, padx=10, pady=3)

        for i in CWJXGUI.uabclist:
            self.uabc_listbox.insert(Tkinter.END, i)
        self.uabc_listbox.bind('<Double-Button-1>', self.uabc_func1)
        self.uabc_listbox.select_set(0)
        self.uabc_listbox.grid(column=2, row=2, rowspan=5, padx=10, pady=10)

        for i in CWJXGUI.ilist:
            self.ii1_listbox.insert(Tkinter.END, i)
        self.ii1_listbox.bind('<Double-Button-1>', self.ii1_func1)
        self.ii1_listbox.grid(column=4, row=2, rowspan=5)

        for i in CWJXGUI.ilist:
            self.ii2_listbox.insert(Tkinter.END, i)
        self.ii2_listbox.bind('<Double-Button-1>', self.ii2_func1)
        self.ii2_listbox.grid(column=6, row=2, rowspan=5)

        self.uabc_button.grid(column=2, row=7, pady=10)
        self.ii1_button.grid(column=4, row=7, pady=10)
        self.ii2_button.grid(column=6, row=7, pady=10)

        self.uabcvar.set('abc')
        self.uabc_chose.grid(column=2, row=8)

        self.ii1var.set('Ia')
        self.ii1_chose.grid(column=4, row=8)

        self.ii2var.set('Ic')
        self.ii2_chose.grid(column=6, row=8)

        self.uabc_xd.grid(column=1, row=8)
        self.ii1_xd.grid(column=3, row=8)
        self.ii2_xd.grid(column=5, row=8)

        self.refresh_button.grid(column=7, row=0, rowspan=12, padx=20)

        self.p1_name.grid(column=8, row=1, pady=3)
        self.p1_name_u.grid(column=9, row=1)
        self.p1_u.grid(column=10, row=1)
        self.p1_name_i1.grid(column=11, row=1)
        self.p1_i1.grid(column=12, row=1)
        self.p1_i1_blank.grid(column=13, row=1, columnspan=3)
        self.p1_name_p.grid(column=9, row=2, pady=3)
        self.p1_p.grid(column=10, columnspan=6, row=2)

        self.p2_name.grid(column=8, row=3, pady=3)
        self.p2_name_u.grid(column=9, row=3)
        self.p2_u.grid(column=10, row=3)
        self.p2_name_i2.grid(column=11, row=3)
        self.p2_i2.grid(column=12, row=3)
        self.p2_i2_blank.grid(column=13, row=3, columnspan=3)
        self.p2_name_p.grid(column=9, row=4, pady=3)
        self.p2_p.grid(column=10, columnspan=6, row=4)

        self.k_name.grid(column=8, row=5, pady=3)
        self.k_name_k.grid(column=9, row=5)
        self.k_k.grid(column=10, row=5, columnspan=6, pady=3)

        self.phi_name.grid(column=8, row=6, pady=3)
        self.phi_name_solo.grid(column=9, row=6)
        self.phi_solo.grid(column=10, row=6)
        self.phi_name_sin.grid(column=11, row=6)
        self.phi_sin.grid(column=12, row=6)
        self.phi_name_cos.grid(column=13, row=6)
        self.phi_cos.grid(column=14, row=6)
        self.phi_blank.grid(column=15, row=6)

        self.k_button.grid(column=8, columnspan=8, row=7, pady=3)

        self.k_result_name.grid(column=8, row=8)
        self.k_result_k.grid(column=9, row=8)
        self.k_result.grid(column=10, row=8, columnspan=6)

        self.rightside.grid(column=16, row=1)

    def uabc_func1(self, event):
        if self.uabc_listbox.curselection() == ():
            self.uabcvar.set('abc')
        else:
            self.uabcvar.set(self.uabc_listbox.get(self.uabc_listbox.curselection()))

    def uabc_func(self):
        if self.uabc_listbox.curselection() == ():
            self.uabcvar.set('abc')
        else:
            self.uabcvar.set(self.uabc_listbox.get(self.uabc_listbox.curselection()))

    def ii1_func1(self, event):
        if self.ii1_listbox.curselection() == ():
            self.ii1var.set('Ia')
        elif self.ii1_listbox.get(self.ii1_listbox.curselection()).replace('-', '') \
                == self.ii2var.get().replace('-', ''):
            tkMessageBox.showinfo('电流输入冲突', 'I1和I2不能相同，请核对输入！')
        else:
            self.ii1var.set(self.ii1_listbox.get(self.ii1_listbox.curselection()))

    def ii1_func(self):
        if self.ii1_listbox.curselection() == ():
            self.ii1var.set('Ia')
        elif self.ii1_listbox.get(self.ii1_listbox.curselection()).replace('-', '') \
                == self.ii2var.get().replace('-', ''):
            tkMessageBox.showinfo('电流输入冲突', 'I1和I2不能相同，请核对输入！')
        else:
            self.ii1var.set(self.ii1_listbox.get(self.ii1_listbox.curselection()))

    def ii2_func1(self, event):
        if self.ii2_listbox.curselection() == ():
            self.ii2var.set('Ic')
        elif self.ii2_listbox.get(self.ii2_listbox.curselection()).replace('-', '') \
                == self.ii1var.get().replace('-', ''):
            tkMessageBox.showinfo('电流输入冲突', 'I1和I2不能相同，请核对输入！')
        else:
            self.ii2var.set(self.ii2_listbox.get(self.ii2_listbox.curselection()))

    def ii2_func(self):
        if self.ii2_listbox.curselection() == ():
            self.ii2var.set('Ic')
        elif self.ii2_listbox.get(self.ii2_listbox.curselection()).replace('-', '') \
                == self.ii1var.get().replace('-', ''):
            tkMessageBox.showinfo('电流输入冲突', 'I1和I2不能相同，请核对输入！')
        else:
            self.ii2var.set(self.ii2_listbox.get(self.ii2_listbox.curselection()))

    def refresh_func(self):
        plt.figure(figsize=(7, 7))
        cw1 = CuoWuJieXian(self.uabcvar.get(), self.ii1var.get(), self.ii2var.get())
        self.p1_u_var.set(cw1.u1)
        self.p1_i1_var.set(cw1.i1)
        p1 = cw1.u1 + '*' + cw1.i1.replace('-', '') + '*cos(' + str(int(cw1.angle()[0])) + u'°+φ)'
        self.p1_p_var.set(p1)

        self.p2_u_var.set(cw1.u2)
        self.p2_i2_var.set(cw1.i2)
        p2 = cw1.u2 + '*' + cw1.i2.replace('-', '') + '*cos(' + str(int(cw1.angle()[1])) + u'°+φ)'
        self.p2_p_var.set(p2)

        k = cw1.cosphi(cw1.angle()[0], cw1.angle()[1])
        self.k_var.set(k)

        cw1.pltpic()

    pattern = re.compile('''(0\.0*[1-9]+)|(([1-8][0-9]|[1-9])(\.[0-9]+){0,1})''')

    def k_func(self):
        phi = self.phi_var.get()
        sinphi = self.sinphi_var.get()
        cosphi = self.cosphi_var.get()
        if phi == '' and sinphi == '' and cosphi == '':
            tkMessageBox.showinfo('输入错误', u'要计算k值必须提供φ角的信息，请填写φ值或者φ的正弦余弦值')
        elif phi != '' and sinphi != '':
            tkMessageBox.showinfo('输入错误', u'φ角的信息不要重复填写，请选择单独填写φ或者填写φ的正弦余弦')
        elif phi != '' and cosphi != '':
            tkMessageBox.showinfo('输入错误', u'φ角的信息不要重复填写，请选择单独填写φ或者填写φ的正弦余弦')
        elif phi == '' and sinphi != '' and cosphi != '':
            _phi = 0
            if float(sinphi) >= 1 or float(sinphi) <= 0 or float(cosphi) >= 1 or float(cosphi) <= 0:
                tkMessageBox.showinfo(u'φ的正弦余弦值输入错误', u'φ的正弦余弦值必须在0-1之间')
            else:
                _sinphi = float(sinphi)
                _cosphi = float(cosphi)
        elif phi != '' and sinphi == '' and cosphi == '':
            if 0 < float(phi) < 90:
                _phi = float(phi)
                _sinphi = ''
                _cosphi = ''
            else:
                tkMessageBox.showinfo(u'φ值输入错误', u'φ值必须在0-90度之间')
        else:
            tkMessageBox.showinfo('输入有误', u'φ的信息输入有误，请仔细核对！')
        cw1 = CuoWuJieXian(self.uabcvar.get(), self.ii1var.get(), self.ii2var.get())
        # 看几个参数是否已定义
        if '_phi' in locals().keys() and '_sinphi' in locals().keys() and '_cosphi' in locals().keys():
            real_k = cw1.real_k(cw1.angle()[0], cw1.angle()[1], _phi, _sinphi, _cosphi)
            self.k_result_var.set(real_k)
        # 没有定义则肯定为上面报错的信息，直接pass或者将k值历史值清除
        else:
            self.k_result_var.set('')


if __name__ == '__main__':
    cwgui1 = CWJXGUI()
    cwgui1.master.title('电能计量错误接线判断')
    cwgui1.mainloop()
