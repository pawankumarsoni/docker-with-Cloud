#!/usr/bin/python36

print("content-type: text/html")
print("")

import subprocess as sp
import cgi
#services = sp.getoutput("rpm -qa")
#j = services.split("\n")
#for i in j:
	#k = i.split()
print("""
<link src='text/css' rel="stylesheet" href="/var/www/html/saas-launch.css">
<form action='bstaas.py'>
<input type='text' name='size' placeholder='enter the size whatever you need : ' />
<input type='submit' />
</form>
""")
	#print("<a href='saas_launch1.py' download>" + "<select><option>" + i +"</option></select>""</a><br />")
	#print("\n")
	#if "firefox" in i:
		#print("<a href='firefox_launch.py'>Click to launch firefox</a>" + " " + i)
