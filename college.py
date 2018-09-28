#!/usr/bin/python36
import subprocess as sp
print("content-type:text/html")
print("\n")
print('''<form action="language_compiler.py">
<h3>Enter your detail</h3></br>
User Name : <input name="uname"></br>
Port Name : <input name="pname"></br>
Which Service you want to get : </br>
<input type="radio" name="one" value="Python" checked> Python<br>
<input type="radio" name="one" value="C"> C <br>
<input type="radio" name="one" value="Python36"> Python36<br>
<input type="radio" name="one" value="C++"> C++<br>
<input type="radio" name="one" value="ruby">Ruby<br>
<input type="submit">
</form>''')
