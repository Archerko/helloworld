# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:backup_ver3.py

import os
import time

# 1,确定哪些需要备份的目录路径
source =['c:\\exp','c:\\exp2']

# 2,确定备份的主目录
target_dir = 'c:\\pybackup\\'

# 3,文件备份成一个7z
# 4，rar命名为按当前日期时间

# 以日期为目录
today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

# 添加用户输入注释
comment = raw_input('Please enter a comment:-->')

# 判断注释是否为0
if len(comment) == 0:
    target = today + os.sep + now + '.7z'
else:
    target = today + os.sep + now + '_'+ comment.replace(' ','_') + '.7z'

# 检查目录是否存在，不存在则进行目录生成
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory',today


# 5,使用rar命令
zip_command = 'c:\\7zip\\7z.exe a "%s" %s'%(target,' '.join(source))

if os.system(zip_command) == 0:
    print "Successful backup to",target
else:
    print "Backup Failed"
