import json 
import re
ui=0
i=0
ai=0
while ui<8 :
   
    
    file_w2= open("EdgeList_"+str(ui)+".txt", "w")
    
    filename = "MAG/mag_papers_"+str(ui)+"/mag_papers_"
    

    total=0
    regexp = re.compile(r'omput')
    
    while i<(ui+1)*20 :
        dummy=str(i)+".txt"
        file_r= open(filename+dummy, "r")
        print(filename+dummy)
        print(str(ai)+" \n ")

        for line in file_r:
            j_content = json.loads(line)
            ref_list=[]
            s='en'
            if "lang" in j_content.keys():
                s=j_content["lang"]
            if "doc_type" in j_content.keys() :
                if j_content["doc_type"]== "Journal" :

                    if "year" in j_content.keys()  :
                        if "references" in j_content.keys() and j_content["year"]>2000 :
                            ref_list=j_content["references"]
                            for i1 in ref_list :
                                file_w2.write(str(j_content["id"])+"  "+str(i1)+"  "+str(j_content["year"])+"\n")
                        ai=ai+1
        i=i+1
    ui=ui+1
    print("EdgeList_"+str(ui)+".txt\n")

    file_w2= open("EdgeList_"+str(ui)+".txt", "w")
    
    filename = "MAG/mag_papers_"+str(ui)+"/mag_papers_"
    

    total=0
    regexp = re.compile(r'omput')
    
    
i=160


file_w2= open("EdgeList_"+str(8)+".txt", "w")
    
filename = "MAG/mag_papers_"+str(8)+"/mag_papers_"


while i<167:
    dummy=str(i)+".txt"
    file_r= open(filename+dummy, "r")
    print(filename+dummy)
    print(str(ai)+" \n ")

    for line in file_r:
        j_content = json.loads(line)
        ref_list=[]
        s='en'
        if "lang" in j_content.keys():
            s=j_content["lang"]
        if "doc_type" in j_content.keys() :
            if j_content["doc_type"]== "Journal" :

                if "year" in j_content.keys()  :
                    if "references" in j_content.keys() and j_content["year"]>2000 :
                        ref_list=j_content["references"]
                        for i1 in ref_list :
                            file_w2.write(str(j_content["id"])+"  "+str(i1)+"  "+str(j_content["year"])+"\n")
                    ai=ai+1
    i=i+1
    
