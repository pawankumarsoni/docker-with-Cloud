#!/usr/bin/python36
import cgi
print("content-type:text/html")
print("\n")
form=cgi.getvalue("software")
if "firefox" in form:
	print("<a href="/root/installsh.tar.gz"></a>")
