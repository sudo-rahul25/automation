#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")
print()



x,y=subprocess.getstatusoutput("sudo ansible-playbook addstorage.yml")
if x==0:
	print("ec2 volume created successfully")
else:
	print("sorry ec2 volume not created")
print("\n")
print()
print(y)
