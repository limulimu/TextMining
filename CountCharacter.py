'''
Created on 15/04/2013

@author: Limu
'''
import json
print "this is a first test!"
d={}
tf=open("pos.txt","r")
for line in tf:
    for a in line:
        if d.has_key(a):
            d[a]+=1
        else:
            d[a]=1
fr=open("alfabat.txt","w")
for key in d:
    fr.write(key)
fr.close()
#json.dump(d,fr)
#
#
#ntf=open("alfabat.txt","r")
#l=ntf.read()
#x=json.loads(l)
#for key in x:
#    print key,x[key]

