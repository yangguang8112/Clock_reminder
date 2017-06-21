#-*- coding:utf-8 -*-
#!/usr/bin/python  
  
import HTMLParser  
import urlparse  
import urllib  
import urllib2  
import cookielib  
import string  
import re  
import sys
import simplejson as json

def check_clock(date_time,work_num):
    date = date_time.split(" ")[0]
    year_moth = "-".join(date.split("-")[:2])
    time = date_time.split(" ")[1].split(":")[0].strip("0")
#
    hosturl = 'http://kq.novogene.com:8080'
    posturl = 'http://kq.novogene.com:8080/selfservice/login/?next=selfservice/'
    cj = cookielib.LWPCookieJar() 
    cookie_support = urllib2.HTTPCookieProcessor(cj) 
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler) 
    urllib2.install_opener(opener) 
    h = urllib2.urlopen(hosturl) 
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1'} 
    postData = {'username' : work_num,'password' : '123456','template9' : '','finnger10' : '','finnger9' : '','template10' : '','login_type' : 'pwd','client_language' : 'zh-cn'} 
    postData = urllib.urlencode(postData) 
    request = urllib2.Request(posturl, postData, headers) 
    response = urllib2.urlopen(request)
##
    postData_table = {'page':'1','rp':'20','sortname':'undefined','sortorder':'undefined','query':'','qtype':'','UserIDs':'1940','ComeTime': year_moth+'-01','EndTime':date}
    table_url = 'http://kq.novogene.com:8080/selfatt/grid/selfatt/CardTimes/'
    postData_table = urllib.urlencode(postData_table)
    req = urllib2.Request(table_url, postData_table, headers)
    text = urllib2.urlopen(req).read()
##
    Clock_dic = json.loads(text)
    clock_time = Clock_dic['rows'][-1]['ClockInTime']
    clock_count = len(clock_time.strip().split(","))
    clock_list = clock_time.strip().split(",")
    if date != Clock_dic['rows'][-1]['card_date']:
        return work_num
    else:
        if int(time)<=12:
            if int(clock_list[0].split(":")[0].strip("0")) > 10:
                return work_num
        elif int(time)>12:
            if len(clock_list[-1].strip()) == 0 or int(clock_list[-1].split(":")[0].strip("0")) < 18 :
                return work_num
