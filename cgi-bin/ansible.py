#!/usr/bin/python36

print("content-type: text/html")
print()
import subprocess as sp
x=sp.getoutput("sudo ansible all -a date")
print(x)

