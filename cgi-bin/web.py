#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")
print()



x,y=subprocess.getstatusoutput("sudo ansible-playbook web.yml")
if x==0:
	print("webserver configured successfully")
else:
	print("sorry webserver configured unsuccessfull")
print("\n")
print()
print(y)

