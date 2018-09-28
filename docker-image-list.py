#!/usr/bin/python36
import subprocess as sp
print("content-type:text/html")
print("\n")

docker_image_list=sp.getoutput("sudo docker images")
docker_image_list=docker_image_list.split("\n")

#print("<pre>")
#for i in docker_image_list[1:]:
#	j=i.split()
#	print(j[0]+":"+j[1])
#print("</pre>")
#'''
print('''
<form action="docker_manage.py">
<table align='center' width='80%' border='2'>
<tr>
<td>Enter ur container name</td>
<td><input name="cname"></td>
</tr>
<tr>
<td>Enter ur image name</td>
''')
print("<td><select name='imgname'>")
for i in docker_image_list[1:]:
	print("<option>")
	#print(docker_image_list)
	j=i.split()
	print(j[0]+":"+j[1])
	print("</option>")
print("</select></td></tr>")

print('''<tr>
<td><input type="submit"></td>
<td><input type="reset"></td>
</tr>''')
print('''</table>
</form>''')
