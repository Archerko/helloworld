#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: using_Tkinter.py
import Tkinter
import tkMessageBox


class Application(Tkinter.Frame):
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.name_input =  Tkinter.Entry(self)
        self.name_input.pack()
        self.alert_button = Tkinter.Button(self, text='Hello', command=self.hello)
        self.alert_button.pack()

    def hello(self):
        name = self.name_input.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()
