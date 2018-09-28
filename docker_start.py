#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type:text/html")
form=cgi.FieldStorage()
cname=form.getvalue('cname')
o=sp.getoutput("sudo docker start {c}".format(c=cname))
#sp.getoutput("/usr/sbin/shellinaboxd")
print("location: http://192.168.43.111/cgi-bin/docker_manage.py")
print("\n")
