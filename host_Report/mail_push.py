#!/usr/bin/env python 
#coding: utf-8 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
import time
import os

BASE = os.path.dirname(os.path.abspath(__file__))

txt='''--------------------------------------------------------------------
load: 系统1分钟，5分钟，15分钟的平均负载
iowait: 显示用于等待I/O操作占用 CPU 总时间的百分比。
irq: 运行队列的长度（等待运行的进程数）
mem free: 内存的可用空间
mem cache: 已使用的cache空间
mem buffer: 已使用的buffer空间
DISK IO: tps：每秒钟物理设备的 I/O 传输总量
         rtps：每秒钟从物理设备读入的数据总量
         wtps：每秒钟向物理设备写入的数据总量
         bread/s：每秒钟从物理设备读入的数据量，单位为 块/s
         bwrtn/s：每秒钟向物理设备写入的数据量，单位为 块/s

Disk space: 磁盘已用空间
PPS: 每秒收到的包数/和发包数
bandwidth: 每秒钟接收的字节数/发送字节数
syslog: 系统日志的报错信息'''
now=time.localtime()

nowtime=str(now[0])+'/'+str(now[1])+'/'+str(now[2])

sender = 'jumpserver@bitnei.cn'
receiver = 'smc@bitnei.cn'
#receiver = 'sunyang@transilink.com'
smtpserver = 'smtp.exmail.qq.com' 
username = '...'
password = '...'

# Create message container - the correct MIME type is multipart/alternative. 
msg = MIMEMultipart('alternative') 
msg['Subject'] = u"北理工西山机房 系统每日分析报告" 


# Create the body of the message (a plain-text and an HTML version). 
lll=file(BASE + '/cc.html').read() 

html = """ 
<html lang="zh"> 
<head>
<style>
body {
	font: normal 11px auto "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
	color: #4f6b72;
	background: #E6EAE9;
}

a {
	color: #c75f3e;
}

#mytable {
	width: 700px;
	padding: 0;
	margin: 0;
}

caption {
	padding: 0 0 5px 0;
	width: 700px;
	font: italic 11px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
	text-align: right;
}

th {
	font: bold 11px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
	color: #4f6b72;
	border-right: 1px solid #C1DAD7;
	border-bottom: 1px solid #C1DAD7;
	border-top: 1px solid #C1DAD7;
	letter-spacing: 2px;
	text-transform: uppercase;
	text-align: left;
	padding: 6px 6px 6px 12px;
	background: #CAE8EA url(images/bg_header.jpg) no-repeat;
}

th.nobg {
	border-top: 0;
	border-left: 0;
	border-right: 1px solid #C1DAD7;
	background: none;
}

td {
	border-right: 1px solid #C1DAD7;
	border-bottom: 1px solid #C1DAD7;
	background: #fff;
	padding: 6px 6px 6px 12px;
	color: #4f6b72;
}


td.alt {
	background: #F5FAFA;
	color: #797268;
}

th.spec {
	border-left: 1px solid #C1DAD7;
	border-top: 0;
	background: #fff url(images/bullet1.gif) no-repeat;
	font: bold 10px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
}

th.specalt {
	border-left: 1px solid #C1DAD7;
	border-top: 0;
	background: #f5fafa url(images/bullet2.gif) no-repeat;
	font: bold 10px "Trebuchet MS", Verdana, Arial, Helvetica, sans-serif;
	color: #797268;
}
    </style>
</head> 
<body> 
<div>
<h1 align="center" style="font-size:36px;">%s</h1> 
</div>
<table id="mytable" border="1" cellspacing="0" summary="The technical specifications of the Apple PowerMac G5 series"> 
%s 
</table> 
</body> 
</html> 
"""%(nowtime,lll)

# Record the MIME types of both parts - text/plain and text/html. 
part2 = MIMEText(html, 'html') 

# Attach parts into message container. 
# According to RFC 2046, the last part of a multipart message, in this case 
# the HTML message, is best and preferred. 
msg.attach(part2) 
#构造附件 
#att = MIMEText(open('/root/cc.xlsx', 'rb').read(), 'base64', 'utf-8') 
#att["Content-Type"] = 'application/octet-stream' 
#att["Content-Disposition"] = 'attachment; filename="check.xlsx"' 
#msg.attach(att) 

smtp = smtplib.SMTP() 
smtp.connect('smtp.exmail.qq.com',25)
smtp.login(username, password) 
smtp.sendmail(sender, receiver, msg.as_string()) 
smtp.quit()


