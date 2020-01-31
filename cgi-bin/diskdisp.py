#!/usr/bin/python36
import subprocess

print("content-type: text/html")
print()

import cgitb
cgitb.enable()
cmd = "sudo fdisk -l"

output = subprocess.getoutput(cmd)
print(output)
print("""
<form action='http://192.168.43.48/cgi-bin/partrmv.py'>
ENTER DEVICE NAME: <input name=u />
<br/>
ENTER PARTITION NO: <input name=v />
<br/>
<br/>
<input type='submit'/>
</form>
""")
