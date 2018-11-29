#!/usr/bin/python
import re
import networkx as nx
import os
with open("acm.txt") as myfile:
       head = myfile.readlines(1000)
print(head)
file = open("ACM_EDGELIST.txt","w") 
with open("acm.txt", encoding="utf8") as f:
    for line in f:
        matchObj = re.match( r'#index(.*?)', line, re.M|re.I)
        if matchObj :
            a=a+1
            rd=int(line[6:].rstrip(os.linesep))
            mainpaper=int(rd)
            #print()
        matchObj2 = re.match( r'#%(.*?)', line, re.M|re.I)
        if matchObj2 :
            #print(line)
            rd=int(line[2:].rstrip(os.linesep))
            
            dummy=int(rd)
            #DG.add_edge(mainpaper,dummy)
            file.write(str(mainpaper)+"   "+ str(dummy)+"\n")
        
paersindex=[]
a=0
b=0
c=0
year="0000"
mainpaper="Main"
dummy="dummy"
#DG=nx.DiGraph()
file = open("ACM_NODES_TIME.txt","w") 
with open("acm.txt", encoding="utf8") as f:
    for line in f:
        matchObj = re.match( r'#t(.*?)', line, re.M|re.I)
        if matchObj :
            a=1
            mainpaper=int(line[2:])
            b=b+1
            #print()
        matchObj2 = re.match( r'#index(.*?)', line, re.M|re.I)
        if matchObj2 :
            #print(line)
            c=c+1
            dummy=int(line[6:])
            if a==0 :
                file.write(str(dummy)+"("+ str("0000")+")\n")
            if a==1 :
                file.write(str(dummy)+"("+ str(mainpaper)+")\n")
                a=0
          
            
            

