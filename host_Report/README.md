# 每日报表生成邮件发送

需要部署到salt服务器上，如果路径不同需要修改 run.sh内的路径
安装salt，sar命令，python的依赖包

安装sar
yum install sysstat -y

拷贝脚本到salt目录

mkdir -p /srv/salt/scripts/
cp /root/put/host_Report/check.sh /srv/salt/scripts/

设置crontab (添加)
cronta -e
40 23 * * * /bin/bash /root/put/host_Report/run.sh >> /tmp/salt_ip.log 2>&1

阀值设置，在check.sh脚本内 修改以下变量即可，根据自己需求
iowait=1
cpuirq=5
load=5
memfree=20
membuffer=0
memcache=0
IOtps=0
IOrtps=0
IOwtps=0
IObread=0
IObwrtn=0
PPS=0
bandwidth=0



正常情况
![image](https://github.com/s57445560/smctool/raw/master/host_Report/img/1.png)


如果超过阈值则会标红
![image](https://github.com/s57445560/smctool/raw/master/host_Report/img/2.png)
