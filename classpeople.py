# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:classpeople.py


class People:
    age_dict={}
    email_dict={}
    phone_dict={}

    def __init__(self,name,age,email,phone):
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone
        self.age_dict[self.name]=age
        self.email_dict[self.name]=email
        self.phone_dict[self.name]=phone

    def SayHi(self):
        print 'Hello,my name is %s'%self.name

    def SearchAge(self,_name):
        if _name in self.age_dict:
            print 'The age of', _name, 'is', self.age_dict[_name]
        else:
            print 'The name is not in the dictory.'

    def SearchEmail(self,_name):
        if _name in self.email_dict:
            print 'The email of', _name, 'is', self.email_dict[_name]
        else:
            print 'The name is not in the dictory.'

    def SearchPhone(self,_name):
        if _name in self.phone_dict:
            print 'The phone of', _name, 'is', self.phone_dict[_name]
        else:
            print 'The name is not in the dictory.'

    def ShowDict(self):
        _show_age = str(self.age_dict)
        print  _show_age
        _len_age = len(self.age_dict)
        print _len_age


def add_people():
    add_name = raw_input('请输入人员姓名:')
    add_age = raw_input('请输入人员年龄：')
    add_email = raw_input('请输入人员电子邮件：')
    add_phone = raw_input('请输入人员电话：')
    if len(add_name)!=0 and len(add_age)!=0 and len(add_email)!=0 and len(add_phone)!=0:
        add_p = People(add_name, add_age, add_email, add_phone)
        add_p.SayHi()
    else:
        print "输入信息有误！"


def del_people():
    del_name = raw_input('请输入要删除的人员姓名：')
    if del_name in People.age_dict:
        del People.age_dict[del_name]
        del People.phone_dict[del_name]
        del People.email_dict[del_name]
    else:
        print '你输入的人员并不在名单里。'


def show_dict():
    _show_age = str(People.age_dict)
    _show_email = str(People.email_dict)
    _show_phone = str(People.phone_dict)
    print _show_age
    print _show_email
    print _show_phone


def search_people():
    _search_name=raw_input('请输入要查找的人员姓名:')
    if _search_name in People.age_dict:
        print 'The age of %s is %s,and the email is %s,and the phone is %s'%(_search_name,People.age_dict[_search_name],People.email_dict[_search_name],People.phone_dict[_search_name])
    else:
        print '你输入的人员不在名单里。'


def save_dict():
    import cPickle as p
    pdict = 'peopledict.data'
    f = file(pdict,'w')
    p.dump(People.age_dict,f)
    p.dump(People.email_dict,f)
    p.dump(People.phone_dict,f)
    f.close()


def switch():
    while True:
        s = raw_input('''\n请问你想做什么？\n1.增加人员\n2.删除人员\n3.查找人员\n4.显示现有名单\n5.保存名录\n6.保存退出\n--->''')
        if s == '1':
            add_people()
        elif s == '2':
            del_people()
        elif s == '3':
            search_people()
        elif s == '4':
            show_dict()
        elif s == '5':
            save_dict()
        elif s == '6':
            save_dict()
            break
        else:
            print '输入错误！请重新输入！'

switch()
