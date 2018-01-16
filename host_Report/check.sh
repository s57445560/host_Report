#!/bin/bash
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




########################################################################################
echo -n "cpu iowait "
sar -u 2>/dev/null|egrep '^[0-9]'|sort -k 6 -rn|awk 'NR==1{b=$6>'$iowait'?$6",":$6;print $1,b}'|egrep '.'
[[ $? == 0 ]]||echo "failed!"



echo -n "cpu irq "
sar -q 2>/dev/null|egrep '^[0-9]'|sort -k 2 -rn|awk 'NR==1{b=$2>'$cpuirq'?$2",":$2;print $1,b}'|egrep '.'
[[ $? == 0 ]]||echo "failed!"


num=`cat /proc/cpuinfo |grep processor|wc -l`
cpunum=`echo "${num}*0.8"|bc`

echo -n "load "
sar -q 2>/dev/null|egrep '^[0-9]'|awk '{a[$0]=$4+$5+$6}END{for(i in a)print i,a[i]}'|sort -k7 -nr|awk 'NR==1{b=$4>'$cpunum'?$4",":$4;print $1,b,$5,$6" cpu-",'$num'}'|egrep '.'
[[ $? == 0 ]]||echo "failed!"

###################################################################################free

echo -n "mem free "
total=`free|awk '$1~/Mem/{print $2}'`
sar -r 2>/dev/null|awk '$1~/^[0-9]/&&$2~/^[0-9]/{a[$1]=$2+$5+$6;print $1,a[$1]}'|sort -n -k2|awk 'NR==1{b=$2*100/'$total'<'$memfree'?$2*100/'$total'"%,":$2*100/'$total'"%";print $1,b,"total="'$total'/1024"M"}'
[[ $? == 0 ]]||echo "failed!"


#echo -n "mem free "
#sar -r 2>/dev/null|awk '$1~/^[0-9]/&&$3~/^[0-9]/'|sort -k3 -n|awk 'NR==1{b=$3/1024<'$memfree'?$3/1024"M,":$3/1024"M";print $1,$2,b}'|egrep '.'
#[[ $? == 0 ]]||echo "failed!"

#echo -n "mem buffer "
#sar -r 2>/dev/null|egrep '^[0-9]'|sort -k6 -nr|awk 'NR==1{print $1,$2,$6/1024"M"}'|egrep '.'
#[[ $? == 0 ]]||echo "failed!"

#echo -n "mem cache "
#sar -r 2>/dev/null|egrep '^[0-9]'|sort -k7 -nr|awk 'NR==1{print $1,$2,$7/1024"M"}'|egrep '.'
#[[ $? == 0 ]]||echo "failed!"


#IO=`sar -d 2>/dev/null|awk '{a[$3]++}END{for(i in a)if(i~/^[d]/)print i}'|egrep '.'`
#[[ $? == 0 ]]||echo "DISK IO failed!"

#for i in $IO;do
#echo -n "DISK IO $i "
#sar -d 2>/dev/null|grep $i|egrep '^[0-9]'|sort -nr -k11|awk 'NR==1{print $1,$2,$3,$11}'|egrep '.'
#[[ $? == 0 ]]||echo "failed!"
#done
#############################################################################IO
echo -n "DISK IO tps "
sar -b|egrep '^[0-9]'|sort -rn -k 2|awk 'NR==1{print $1,$2}'
[[ $? == 0 ]]||echo "failed!"

echo -n "DISK IO rtps "
sar -b|egrep '^[0-9]'|sort -rn -k 3|awk 'NR==1{print $1,$3}'
[[ $? == 0 ]]||echo "failed!"


echo -n "DISK IO wtps "
sar -b|egrep '^[0-9]'|sort -rn -k 4|awk 'NR==1{print $1,$4}'
[[ $? == 0 ]]||echo "failed!"

echo -n "DISK IO bread/s "
sar -b|egrep '^[0-9]'|sort -rn -k 5|awk 'NR==1{print $1,$5}'
[[ $? == 0 ]]||echo "failed!"

echo -n "DISK IO bwrtn/s "
sar -b|egrep '^[0-9]'|sort -rn -k 6|awk 'NR==1{print $1,$6}'
[[ $? == 0 ]]||echo "failed!"

df -hP |awk '+$5>85{print "Disk space "$0","}'|egrep '.'
[[ $? == 0 ]]||echo "Disk space ok!"


###################################################################################

eth=`sar -n DEV 2>/dev/null|awk '{a[$2]++}END{for(i in a)if(i~/^[a-z]+[0-9].*/)print i}'|egrep '.'`
[[ $? == 0 ]]||echo "PPS failed!"


for i in $eth
do
echo -n "PPS $i "
sar -n DEV 2>/dev/null|grep $i|egrep  '^[0-9]' |awk '{a[$0]=$4+$5}END{for(i in a)print i,a[i]}'|sort -rn -k11|awk 'NR==1{print $1,$2,$3,$4"/"$5}'|egrep '.'
[[ $? == 0 ]]||echo "failed!"
done


for i in $eth;do
echo -n "bandwidth $i "
sar -n DEV 2>/dev/null|grep $i|egrep  '^[0-9]' |awk '{a[$0]=$6+$7}END{for(i in a)print i,a[i]}'|sort -rn -k11|awk 'NR==1{print $1,$2,$3,$6"/"$7}'|egrep '.'
[[ $? == 0 ]]||echo "failed!"
done

da=`date +%d`
day=`echo $da|sed 's/^0//g'`

#echo -n "syslog "
#syslog=`egrep -i '(err|error|fail)' /var/log/messages|egrep -v -i "(gmetad|nagios)"|egrep "^[a-zA-Z ]+$day"`

#if [[ $? == 1 ]];then
#echo "OK!"
#else
#echo $syslog","
#fi

echo -n "syslog "
syslog=`egrep -i '(err|error|fail)' /var/log/messages|egrep -v -i "(gmetad|nagios|ldap)"|egrep "^[a-zA-Z ]+$day "`
num=`egrep -i '(err|error|fail)' /var/log/messages|egrep -i "ldap"|egrep "^[a-zA-Z ]+$day "|awk 'END{print NR}'`
syslog1=`egrep -i '(err|error|fail)' /var/log/messages|egrep -i "ldap"|egrep "^[a-zA-Z ]+$day "|awk 'NR==1'|egrep '.'`

if [[ $? == 1 && $syslog == '' ]];then
echo "OK!"
else
echo -n $syslog","
echo $syslog1"=="$num 
fi
