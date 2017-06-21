# -*- coding: utf-8 -*-
import itchat
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import commands

def send_wechat(work_num):
    date = commands.getoutput('date "+%Y-%m-%d %H:%M:%S"') 
    itchat.auto_login(hotReload=True,enableCmdQR=2)
    for people in work_num:
        itchat.send(people+',请注意,没有打卡\n'+date+'\n本消息自动发送,请勿回复\n如若信息有误,请联系yangguang@novogene.com', toUserName=people)
