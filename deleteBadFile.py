#coding:UTF-8

"""
本程序用作删除data目录下非DISCUZ系统自带的文件
即黑客上传的恶意/广告文件等
"""

import os

goodFileLists=[
	'attachment',
	'cache',
	'diy',
	'sysdata',
	'template',
	'threadcache',
	'updatetime.lock',
	'sendmail.lock',
]
path="/web/bbs/data"

fps=os.listdir(path)
for fp in fps:
	badSign=True
	for goodFileName in goodFileLists:
		if fp == goodFileName:
			badSign=False
			break
	if badSign:
		os.system("rm -rf %s/%s"%(path,fp))		
