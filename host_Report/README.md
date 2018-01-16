# 每日报表生成邮件发送

需要部署到salt服务器上，如果路径不同需要修改 run.sh内的路径<br>
安装salt，sar命令，python的依赖包<br>
<br>
安装sar<br>
yum install sysstat -y<br>

拷贝脚本到salt目录<br>
<br>
mkdir -p /srv/salt/scripts/ <br>
cp /root/put/host_Report/check.sh /srv/salt/scripts/<br>

设置crontab (添加)<br>
cronta -e<br>
40 23 * * * /bin/bash /root/put/host_Report/run.sh >> /tmp/salt_ip.log 2>&1

阀值设置，在check.sh脚本内 修改以下变量即可，根据自己需求<br>
iowait=1<br>
cpuirq=5<br>
load=5<br>
memfree=20<br>
membuffer=0<br>
memcache=0<br>
IOtps=0<br>
IOrtps=0<br>
IOwtps=0<br>
IObread=0<br>
IObwrtn=0<br>
PPS=0<br>
bandwidth=0<br>



正常情况
![image](https://github.com/s57445560/smctool/raw/master/host_Report/img/1.png)


如果超过阈值则会标红
![image](https://github.com/s57445560/smctool/raw/master/host_Report/img/2.png)
