# -*- coding:utf-8 -*-
# Filename;map.py

a = [1, 4, 6, 8, 9]

b = map(str, a)
print b

x = ['adam', 'LISA', 'barT']


def change_name(nm):
    name = list(nm)
    if name[0].lower() == name[0]:
        name[0] = name[0].upper()          # 注意这里的upper()和lower()都不要忘了最后的()
    for i in range(1, len(name)):
        if name[i].upper() == name[i]:
            name[i] = name[i].lower()
    names = "".join(name)
    return names

y = map(change_name, x)
print y
