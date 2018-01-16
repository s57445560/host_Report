#!/bin/bash

fabric_path='/root/put/host_Report/'

python2.6 ${fabric_path}salt_get_host_info.py

python2.6 ${fabric_path}mail_push.py

if [[ $? != 0 ]]
then
    sleep 30
    python2.6 ${fabric_path}mail_push.py
else
    exit 0
fi

if [[ $? != 0 ]]
then
    sleep 30
    python2.6 ${fabric_path}mail_push.py
else
    exit 0
fi

if [[ $? != 0 ]]
then
    sleep 30
    python2.6 ${fabric_path}mail_push.py
else
    exit 0
fi

if [[ $? != 0 ]]
then
    sleep 30
    python2.6 ${fabric_path}mail_push.py
else
    exit 0
fi
