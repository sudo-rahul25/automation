#!/usr/bin/python36

print("content-type: text/html")
print()
 

import subprocess as sp
x=sp.getoutput("date")
print(x)
print("helloo , you are viewing dateof server")
