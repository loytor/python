#!/usr/bin/python
# coding=utf-8

import os

msg = raw_input('commit message：')

os.system('git status')
os.system('git pull')
os.system('git add .')
os.system('git commit -m ' + msg )
os.system('git push')