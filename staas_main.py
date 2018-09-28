#!/usr/bin/python36
print("content-type:text/html")
print("\n")
print('''
<form action=staas_code.py>
<table align='center' width='80%' border='2'>
<tr>
<td>UserName</td>
<td><input name="uname"></td>
</tr>
<tr>
<td>Size required (in MB)</td>
<td><input name="sname"></td>
</tr>
''')
print('''<tr>
<td><input type="submit"></td>
<td><input type="reset"></td>
</tr>
</table>
</form>
''')
