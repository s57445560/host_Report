#!/usr/bin/python
import re,os
fabric_path = os.path.dirname(os.path.abspath(__file__)) + "/"

class Html_create(object):
    def __init__(self,data):
        self.ip_list = []
        self.salt_all_ip = []
        self.head = ['ip','system load','cpu iowait','cpu irq','mem free','DISK IO','Disk space','PPS','bandwidth','syslog']
        self.data = data
        salt_ip_result = os.popen("salt-key -L")
        for i in salt_ip_result.readlines():
            if i.strip("\n") == "Denied Keys:":
                break
            if i.strip("\n") == "Accepted Keys:":
                continue
            self.salt_all_ip.append(i.strip("\n"))

        self.html_file = open(fabric_path+'cc.html','w+')

        self.ww(self.head,first=True)
        self.num = 0
        for k in self.salt_all_ip:
            if k not in self.data:
                self.ip_list.append(k)
                for i in self.head[1::]:
                    self.ip_list.append('')
            else:
                for head_e in self.head:
                    if 'ip' == head_e:
                        self.ip_list.append(k)
                        continue
                    rp = re.compile(r'(?<=%s ).*' % head_e)
                    self.ip_list.append('<br/>'.join(rp.findall(self.data[k]["stdout"])))
            if self.num%2 == 0:
                self.ww(self.ip_list)
            else:
                self.ww(self.ip_list,color=True)
            self.ip_list = []
            self.num += 1

    def ww(self, l,first=False,color=False):
        if first:
            self.html_file.write('<tr style="background-color: #dedede;border-color: #666666;border-style: solid;border-width: 1px;">\n')
            for i in l:
                self.html_file.write('<th scope="col">%s<th>\n'%i)
        else:
            self.html_file.write('<tr>\n')
            if color:
                self.w(l,color=True)
            else:
                self.w(l)
        self.html_file.write('</tr>\n')

    def w(self, ll,color=False):
        num=0
        self.html_file.write('<th >%s<th>\n'%''.join(ll[:1]))
        if len([x for x in ll[1:] if x!=''])==0:
            #self.html_file.write('<td >%s<td>\n'%''.join(ll[:1]))
            for i in range(len(self.head[1:])):
                self.html_file.write('<td style="background-color: red">%s<td>\n'%'ssh timeout')
            return
        for i in ll[1::]:
            if ',' in i:
                self.html_file.write('<td style="background-color: red">%s<td>\n'%i)
            else:
                if color:
                    self.html_file.write('<td class="alt">%s<td>\n'%i)
                else:
                    self.html_file.write('<td>%s<td>\n'%i)


