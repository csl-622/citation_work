import json

file=open("dblp-ref/dblp-ref-0.json","r")

Refers=[]
i=0
id="000000000000"

file = open("DBLP_EDGES0.txt","w")

with open("dblp-ref/dblp-ref-0.json", encoding="utf8") as f:
    for line in f:
        dictionary = json.loads(line)
        #print(line)
        id=dictionary['id']
        if 'references' in dictionary :
            Refers=dictionary['references']
            for re in Refers :
                file.write(str(id)+"   "+ str(re)+"\n")
        

Refers=[]
i=0
id="000000000000"
file = open("DBLP_EDGES1.txt","w")
with open("dblp-ref/dblp-ref-1.json", encoding="utf8") as f:
    for line in f:
        dictionary = json.loads(line)
        #print(line)
        id=dictionary['id']
        if 'references' in dictionary :
            Refers=dictionary['references']
            for re in Refers :
                file.write(str(id)+"   "+ str(re)+"\n")
        

Refers=[]
i=0
id="000000000000"
file = open("DBLP_EDGES2.txt","w")
with open("dblp-ref/dblp-ref-2.json", encoding="utf8") as f:
    for line in f:
        dictionary = json.loads(line)
        #print(line)
        id=dictionary['id']
        if 'references' in dictionary :
            Refers=dictionary['references']
            for re in Refers :
                file.write(str(id)+"   "+ str(re)+"\n")
        

Refers=[]
i=0
id="000000000000"
file = open("DBLP_EDGES3.txt","w")
with open("dblp-ref/dblp-ref-3.json", encoding="utf8") as f:
    for line in f:
        dictionary = json.loads(line)
        #print(line)
        id=dictionary['id']
        if 'references' in dictionary :
            Refers=dictionary['references']
            for re in Refers :
                file.write(str(id)+"   "+ str(re)+"\n")
        

Refers=[]
i=0
year=0
id="000000000000"
file = open("DBLP_NODES.txt","w")
with open("dblp-ref/dblp-ref-0.json", encoding="utf8") as f:
    for line in f:
        dictionary = json.loads(line)
        #print(line)
        id=dictionary['id']
        if 'year' in dictionary :
            #print("jififof")
            year=dictionary['year']
            file.write(str(id)+"   "+ str(year)+"\n")
        else :
            file.write(str(id)+"   "+ str("0000")+"\n")
        

Refers=[]
i=0
year=0
id="000000000000"
file = open("DBLP_NODES.txt","a")
with open("dblp-ref/dblp-ref-1.json", encoding="utf8") as f:
    for line in f:
        dictionary = json.loads(line)
        #print(line)
        id=dictionary['id']
        if 'year' in dictionary :
            #print("jififof")
            year=dictionary['year']
            file.write(str(id)+"   "+ str(year)+"\n")
        else :
            file.write(str(id)+"   "+ str("0000")+"\n")
        

Refers=[]
i=0
year=0
id="000000000000"
file = open("DBLP_NODES.txt","a")
with open("dblp-ref/dblp-ref-2.json", encoding="utf8") as f:
    for line in f:
        dictionary = json.loads(line)
        #print(line)
        id=dictionary['id']
        if 'year' in dictionary :
            #print("jififof")
            year=dictionary['year']
            file.write(str(id)+"   "+ str(year)+"\n")
        else :
            file.write(str(id)+"   "+ str("0000")+"\n")
        

Refers=[]
i=0
year=0
id="000000000000"
file = open("DBLP_NODES.txt","a")
with open("dblp-ref/dblp-ref-3.json", encoding="utf8") as f:
    for line in f:
        dictionary = json.loads(line)
        #print(line)
        id=dictionary['id']
        if 'year' in dictionary :
            #print("jififof")
            year=dictionary['year']
            file.write(str(id)+"   "+ str(year)+"\n")
        else :
            file.write(str(id)+"   "+ str("0000")+"\n")
        
