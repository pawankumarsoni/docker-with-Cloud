#!/usr/bin/python36
import subprocess as sp
import cgi
print("content-type:/text/html")
form=cgi.FieldStorage()
cname=form.getvalue('cname')
imgname=form.getvalue('imgvalue')
o=sp.getoutput("sudo docker stop {c}".format(c=cname))
print("location: http://192.168.43.111:/cgi-bin/docker_manage.py")
print("\n")
