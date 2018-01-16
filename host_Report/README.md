# 每日报表生成邮件发送

需要部署到salt服务器上，如果路径不同需要修改 run.sh内的路径

设置crontab (添加)

cronta -e

40 23 * * * /bin/bash /root/put/fabric/run.sh >> /tmp/salt_ip.log 2>&1
