#!/usr/bin/python2.6

import salt.client
import html_make
local = salt.client.LocalClient()
result = local.cmd('*', 'cmd.script', ['salt://scripts/check.sh'])

#for k,v in result.items():
#    print(k)
#    print(v["stdout"].split("\n"))


obj = html_make.Html_create(result)
