#!/usr/bin/python
# -*- coding: UTF-8 -*-

# @author:loytor
# @date:2016-02-19 15:10
# @desc: 简单的用户注册程序,需要创建一个users表

'''
CREATE TABLE `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(16) NOT NULL DEFAULT '',
  `pwd` varchar(16) NOT NULL DEFAULT '',
  `create_time` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
'''

import traceback # 捕捉异常
import MySQLdb
import time
import getpass
import datetime

db = MySQLdb.connect("127.0.0.1","root","123321","python" ) #mysql资料
cursor = db.cursor()

# 组织插入点数据
name = raw_input('输入您的用户名:')
pwd = getpass.getpass('输入您的密码:')
time = int(time.time())

# 检测密码长度
if len(pwd) < 6 or len(pwd) > 16 :
	exit('请输入6-16位数有效密码长度')

# 检测用户名称是否重复
sql = "select id FROM users where name='%s'" %name

print '----查询数据库资料----'
cursor.execute(sql)
result = cursor.fetchone()
if result != None:
	exit(name+'账号已被注册')
else:
	print '----用户注册中----'

# 组织sql语句
sql = "INSERT INTO users(name, pwd, create_time) VALUES( '%s' , '%s', %d ) " %(name, pwd, time)

try:
	print '----执行sql语句----'
	cursor.execute(sql)
	db.commit()
except:
	print '----操作失败，数据回滚----'
	db.rollback()
	traceback.print_exc()

# 查询所有账户
sql = "select * from users"
cursor.execute(sql)
results = cursor.fetchall()
print '|--------------------------|'
print '|----ID|账号|密码|创建时间----'
for row in results:
	id = row[0]
	name = row[1]
	pwd = row[2]
	timeStamp = row[3]
	dateArray = datetime.datetime.utcfromtimestamp(timeStamp)
	otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
	# 打印结果
	print "|----%s|%s|%s|%s" % \
		(id, name, pwd, otherStyleTime)

db.close()