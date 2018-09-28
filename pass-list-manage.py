#!/usr/bin/python36


import subprocess as sp
import cgi
import os
print("content-type:text/html")
print("\n")
print('''<center>python2</center></br>
	<center>username python </br>password python</center></br>''')
print('<center>python36</center></br><center>username python36 </br>  password python36</center>')
print("<center><iframe name='cframe' width='80%' height='60%'></iframe></center>")


form=cgi.FieldStorage()
cname=form.getvalue("cname")
imgname=form.getvalue("imgname")
sp.getoutput("sudo docker run -dit --name {c} -p 3000:4200 {i}".format(c=cname,i=imgname))
#print("hi")
list_images=sp.getoutput("sudo docker ps  --format 'table {{.Image}}'")
list_names=sp.getoutput("sudo docker ps  --format 'table {{.Names}}'")
list_status=sp.getoutput("sudo docker ps  --format 'table {{.Status}}'")
list1_images=list_images.split('\n')
list1_names=list_names.split('\n')
list1_status=list_status.split('\n')

#list= str(sp.getoutput("sudo docker ps -a --format 'table'"))
#flist=list.split("\n")

print("<br></br><br></br>")
print('''<table align='center' width='90%' border='2'>
<th>IMAGE NAME</th>
<th>CONTAINER NAME</th>
<th>STATUS</th>
<th>START/STOP</th>
<th>CONSOLE</th>
''')
#print("<table align='center' width='90%' border='2'>")
for i,j,k in zip(list1_images[1:],list1_names[1:],list1_status[1:]):
	#j=i.split()
	print("<tr><td>")
	print(i)
	print("</td>")
	print("<td>"+j+"</td>")
	if 'Exited' in k:
		str="<td>Down</td>"
		print(str)
	elif 'Up' in k:
		str="<td>Up</td>"
		print(str)
	else:
		str="<td>Unknown</td>"
		print(str)
	if 'Up' in str:
		print("<td> <a href='docker_stop.py?cname={}'>stop</a></td>".format(j))
	elif 'Down' in str:
		print("<td> <a href='docker_start.py?cname={}'>start</a></td>".format(j))
	else:
		print("<td>Nothing</td>")
         
	if 'Up' in str:
		sp.getoutput("systemctl restart shellinaboxd")
		print("<td><a target='cframe' href='http://192.168.43.251:3000'>Get</a></td></tr>")
		
	else:
		print("<td><a target='cframe' title='First start it'>Get</a></td></tr>")
print("</table>")
