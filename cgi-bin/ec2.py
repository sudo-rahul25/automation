#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")
print()

#mydata=cgi.FieldStorage()
#r=mydata.getvalue('u')
#print(r)
#print("hello")
#f1=open("vars.yml",'w')
#f1.write("uname: %s"%(r))
#f1.close()

x,y=subprocess.getstatusoutput("sudo ansible-playbook ec2.yml")
if x==0:
	print("ec2 instance created successfully")
else:
	print("sorry ec2 instance not created")
print("\n")
print()
print(y)

