#!/usr/bin/python36
import cgi
import subprocess as sp
print("content-type:text/html")
print("\n")

uname="yu"
passwd="yu"
service="firefox"
sp.getstatusoutput("sudo su - ansible")
sp.getstatusoutput("sudo ansible-playbook /home/ansible/pb1.yml")

#run_ansible=sp.getstatusoutput("sudo ansible-playbook /home/ansible/cloud_services/saas.yml --extra-values username="+ uname+"passwd="+passwd+"service="+service)

print ("""
<form action ="saas_manage.py">
username: <input type='text' name:'uname'>
<br/>
password: <input type='password'>
<br />
Select the software you want to use:
<br />
<select name = 'city'>
<option>firerfox</option>
<option>gedit</option>
<option>vlc media player</option>
</select>""")



