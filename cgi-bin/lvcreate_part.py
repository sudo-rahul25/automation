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
vgname=mydata.getvalue('a')
pvname=mydata.getvalue('b')
lvname=mydata.getvalue('f')
lvsize=mydata.getvalue('c')
lvpath=mydata.getvalue('d')
mntpnt=mydata.getvalue('e')


print("hello")
f1=open("vars.yml",'w')
f1.write("devname: %s\npartno: %s\npartsize1: %s\npartsize2: %s\nvgname: %s\npvname: %s\nlvname: %s\nlvsize: %s\nlvm_path: %s\nmountpoint1: %s"%(dev,pno,start,end,vgname,pvname,lvname,lvsize,lvpath,mntpnt))
f1.close()


x,y=subprocess.getstatusoutput("sudo ansible-playbook lvcreate_part.yml")
if x==0:
        print("LVM created successfully")
else:
        print("sorry LVM not created")
print("\n")
print()
print(y)
print("location: http://192.168.43.48/home.html")
print("")
