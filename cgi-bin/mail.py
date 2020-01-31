#!/usr/bin/python36
import subprocess
import cgi

print("content-type: text/html")
print()

mydata=cgi.FieldStorage()
mail=mydata.getvalue('u')
body=mydata.getvalue('v')
print(mail)
print()
print(body)
print()
f1=open("vars.yml",'w')
f1.write("mail: %s\nbody: %s"%(mail,body))
f1.close()

x,y=subprocess.getstatusoutput("sudo ansible-playbook mail.yml")
if x==0:
        print("mail sent successfully")
else:
        print("sorry mail not sent")
print()
print()
print(y)

