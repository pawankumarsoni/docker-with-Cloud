#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print('\n')

print("hi")

form = cgi.FieldStorage() 
uname=form.getvalue('uname')
logins="no"

res=sp.getstatusoutput("sudo ansible-playbook iscsiclientlogout.yml --extra-vars='ipaddress_target=192.168.43.119 target_name={target} login={login}' ".format(target=uname,login=logins))
if res[0]==0:
	print("You are logged out successfully")
else:
	print("Their is some error logging out")
