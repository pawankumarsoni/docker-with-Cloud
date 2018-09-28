#!/usr/bin/python36

import cgi
import subprocess as sp

print("content-type: text/html")
print('\n')

print("hi")

form = cgi.FieldStorage() 
uname=form.getvalue('uname')
diskspace = form.getvalue('diskspace')
matrix= form.getvalue('matrix')
ip=form.getvalue('ip')
passwd=form.getvalue('passwd')

print("You selected {0} {1} and your IP is: {2}".format(diskspace,matrix,ip))

fh = open('/etc/ansible/allhosts/webhosts/hosts','a+')
fh.write('[iscsiclient] \n{0} ansible_ssh_user=root ansible_ssh_pass={1}\n'.format(ip,passwd))
fh.close()

#print("hi")
login="yes"

res = sp.getstatusoutput("sudo ansible-playbook iscsiclient.yml --extra-vars='ipaddress_target=192.168.43.119 target_name={target} login={login}' ".format(target=uname,login=login))

#print("2")
if res[0]==0:
	print("We have successfully added the disk to your system")
	print("You can use it as per your convience now")
	print("Please change your root's password now")
	print("<form action='BlockStoragelogout.py'>")
	x=uname
	print("<input type='hidden' name='uname' value={0} />".format(x))
	print("<input type=submit name='logout'/>")
	print("</form>") 
else:
	print("Sorry we are unable to process your request")
