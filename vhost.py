#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @author:loytor
# @date:2016-02-17 17:55

import os
if os.getenv("USER") != 'root' :
	print '------------------------------------------------------------------------'
	print '⚠️ 权限不足，需要root用户权限'
	print '------------------------------------------------------------------------'
	exit()

path = raw_input('请输入文件路径:');
domain = raw_input('请输入域名：')

if ( path == '' ) or ( domain == '' ) :
	print '文件路径和域名都不能为空'
	exit() 
else :
	print '------------------------------------------------------------------------'
	print '⌛ 正在验证文件路径是否正常⌛'
	print '------------------------------------------------------------------------'
	if os.path.exists(path):
		print '路径正常⬇️'
	else:
		exit('⚠️ 文件路径不存在')
	print '------------------------------------------------------------------------'
	print '️当前路径是：' , path
	print '当前域名是：' , domain
	
	confirm = raw_input('确定使用当前域名创建虚拟主机吗？y/n：')
	if confirm == 'y' :
		f = file("/etc/apache2/extra/httpd-vhosts.conf","a+")

		txt = '<VirtualHost *:80>',"\n"
		txt += '    ServerAdmin loytor@sina.com',"\n"
		txt += '    DocumentRoot "',path,'"',"\n"
		txt += '    ServerName ',domain, "\n"
		txt += '    ErrorLog "/private/var/log/apache2/dummy-host2.example.com-error_log"',"\n"
		txt += '    CustomLog "/private/var/log/apache2/dummy-host2.example.com-access_log" common',"\n"
		txt += '</VirtualHost>',"\n"
		f.writelines(txt)
		f.close()
		print 'http-vhost.conf写入完成...'
		print '------------------------------------------------------------------------'
		f = file("/etc/hosts","a+")
		txt = '127.0.0.1	', domain ,"\n"
		f.writelines(txt)
		f.close()
		print 'host写入完成...'
		print '------------------------------------------------------------------------'

		reboot = raw_input('是否重启Apache(y/n):')
		if reboot == 'y':
			os.system('apachectl restart')
		else :
			print '------------------------------------------------------------------------'
			exit('请手动重启Apache')
	else :
		exit('终止程序')
