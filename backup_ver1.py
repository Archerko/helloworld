# -*- coding: utf-8 -*-
# !/c:/Python27
# Filename:backup_ver1.py

import os
import time

# 1,确定哪些需要备份的目录路径
source =['c:\\exp','c:\\exp2']

# 2,确定备份的主目录
target_dir = 'c:\\pybackup\\'

# 3,文件备份成一个7z
# 4，rar命名为按当前日期时间
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.7z'

# 5,使用rar命令
zip_command = 'c:\\7zip\\7z.exe a "%s" %s'%(target,' '.join(source))

if os.system(zip_command) == 0:
    print "Successful backup to",target
else:
    print "Backup Failed"