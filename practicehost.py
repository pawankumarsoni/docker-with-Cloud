#!/usr/bin/python36
print("content-type:text/html")
print("\n")
str="[data_ip]\n192.168 ssh=root pass=123\n192.168 ssh=root pass=123"
fh=open('/etc/ansible/hosts','a+')
fh.write(str)
fh.close()
