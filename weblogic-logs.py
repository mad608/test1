# code: weblogic.py
# date: Jan 27, 2016
#
#   find lines with 64.73.11.254,convert each line to a list and pull src ip    and counts
#
#!/usr/bin/env python3.4
import re

mylist=[]
myD= dict()
# find my dstip, the next ip is the src ip. pull the src ip
myip_regex=('199.185.97.2,([0-9.]+)')

fn = ('pa-short.log')
fh = open(fn)

for line in fh:
    line = line.rstrip()
    x = re.findall(myip_regex, line)
    if len(x) > 0:
        #print(x)
        mylist.append(x)

for item in mylist:
    #print(item,type(item))
    mystring= ''.join(item)
    myD[mystring] = myD.get(mystring,0) +1
    #print(mystring)
    #if mystring not in myD:
    #    myD[mystring] = 1
    #else:
    #    myD[mystring] = myD[mystring] + 1

#print(myD)

for key in sorted(myD.keys()):
    print(myD[key], key)
