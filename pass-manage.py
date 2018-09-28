#!/usr/bin/python36


import subprocess as sp
import cgi
import os
print("content-type:text/html")
print("\n")


print('<center>python2</center><br></br><center>username python </br>  password python</center>')
print("<br></br>")
print('<center>python36</center><br></br><center>username python36 </br>  password python36</center>')
print("<br></br>")
#print("<center><iframe name='cframe' width='80%' height='60%'></iframe></center>")
form=cgi.FieldStorage()
cname=form.getvalue("cname")
imgname=form.getvalue("imgname")
sp.getoutput("sudo docker run -dit --name {c} -p 3000:4200 {i}".format(c=cname,i=imgname))
#list_images=sp.getoutput("sudo docker ps  --format 'table {{.Image}}'")
#list_names=sp.getoutput("sudo docker ps  --format 'table {{.Names}}'")
#list_status=sp.getoutput("sudo docker ps  --format 'table {{.Status}}'")
#list1_images=list_images.split('\n')
#list1_names=list_names.split('\n')
#list1_status=list_status.split('\n')
#list= str(sp.getoutput("sudo docker ps -a --format 'table'"))
#flist=list.split("\n")
