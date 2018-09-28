#!/usr/bin/python36
import cgi
import subprocess as sp
print("content-type:text/html")
print("\n")
form=cgi.FieldStorage()
lvm_name=form.getvalue("uname")
lvm_size=form.getvalue("sname")
#print(lvm_name)
#print(lvm_size)
p=sp.getstatusoutput("sudo ansible-playbook lvmAnsible.yml --extra-vars='lvm_size={} lvm_name={}'".format(lvm_size,lvm_name))
sp.getoutput("sudo ansible-playbook lvmMount.yml")
print("<h1>You have received disk name {} having {}MB storage from 192.168.43.111 successfully</h1>".format(lvm_name,lvm_size))
#print(p[0])
#print(p[1])
