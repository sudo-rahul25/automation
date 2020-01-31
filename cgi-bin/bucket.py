#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")
print()

mydata=cgi.FieldStorage()
r=mydata.getvalue('u')
print(r)
print("hello")
f1=open("vars.yml",'w')
f1.write("bucname: %s"%(r))
f1.close()

x,y=subprocess.getstatusoutput("sudo ansible-playbook bucket.yml")
if x==0:
	print("bucket created successfully")
else:
	print("sorry bucket not created")
print("\n")
print()
print(y)

