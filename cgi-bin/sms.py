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
f1.write("msg: %s"%(r))
f1.close()

x,y=subprocess.getstatusoutput("sudo ansible-playbook sms.yml")
if x==0:
        print("sms successfully")
else:
        print("sorry sms not sent")
print("\n")
print()
print(y)

