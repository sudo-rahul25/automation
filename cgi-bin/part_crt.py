#!/usr/bin/python36
import subprocess
import cgi

print("content-type: text/html")
print()

mydata=cgi.FieldStorage()
dev=mydata.getvalue('u')
pno=mydata.getvalue('v')
start=mydata.getvalue('x')
end=mydata.getvalue('y')
print("hello")
f1=open("vars.yml",'w')
f1.write("devname: %s\npartno: %s\npartsize1: %s\npartsize2: %s"%(dev,pno,start,end))
f1.close()

x,y=subprocess.getstatusoutput("sudo ansible-playbook partcrt.yml")
if x==0:
        print("partition created successfully")
else:
        print("sorry partition not created")
print("\n")
print()
print(y)
print("location: http://192.168.43.48/home.html")
print("")
