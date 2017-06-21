#-*- coding:utf-8 -*-
#!/usr/bin/python
import check_clock
import send_wechat
import commands
import os

wfile = open("work_num.txt",'r')
date = commands.getoutput('date "+%Y-%m-%d %H:%M:%S"')
wechat_users = []
for line in wfile:
    work_num = line.strip().split("\t")[0]
    wechat_num = line.strip().split("\t")[1].strip("\n")
    clock_status = check_clock.check_clock(date,work_num)
    if clock_status != None:
        wechat_users.append(wechat_num)
wfile.close()
send_wechat.send_wechat(wechat_users)
