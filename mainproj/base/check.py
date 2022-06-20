import os

n=3
i=1
d=""
while i<n:
    cmd="ls"
    abc=os.popen(cmd)
    d+="\n"+abc.read()
    i+=1
 
print(d)