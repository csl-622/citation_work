import requests
import xml.etree.ElementTree as ET
import networkx as nx
import matplotlib.pyplot as plt
import pickle

def loadData(G,string): 
	url='https://api.elsevier.com/content/abstract/scopus_id/'+string+'?apiKey=2218349f3e862aa0844d7967b1401825&view=REF'
	print url
	resp = requests.get(url)
	if resp.status_code != 200:
		print "Some thing went wrong!!"
		return
	# saving the xml file 
	with open('topnewsfeed.xml', 'wb') as f: 
		f.write(resp.content) 
	parseXML('topnewsfeed.xml',G,string)
def parseXML(xmlfile,G,string):
	tree = ET.parse(xmlfile) 
	root = tree.getroot()
	newsitems = []
	if root.tag=='service-error':
		print "Node does not exists!!"
		return
	count=0
	G.add_node(int(string))
	for child in root:
		count+=1
	if count==0:
		print "No Edge for this node"
		return
	for child in root:
		for childchild in child:
			for ccc in childchild :
				index = 0
				tag=ccc.tag
				while index < len(tag):
					letter = tag[index]
					index = index + 1
					if letter=='}':
						break;
				if tag[index:]=='scopus-id':
					print ccc.text
					G.add_node(int(ccc.text))
					G.add_edge(int(string),int(ccc.text))
def main(): 
	G=nx.DiGraph()
	i=0
	Dict={}
	while True:
		resp = requests.get("http://api.elsevier.com/content/search/scopus?query=SUBJ=CHEM&start="+str(i)+"&field=dc:identifier&count=1",
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': '2218349f3e862aa0844d7967b1401825'})

		results = resp.json()
		if "entry" in results['search-results']:
			for r in results['search-results']["entry"]:
				print str(r['dc:identifier'])[10:]
				Dict[str(r['dc:identifier'])[10:]]=1
				with open("test.txt", "wb") as fp:   #Pickling
					pickle.dump(list(Dict.keys()), fp)	
		else:
			break	
		i=i+1
		print i
	l=list(Dict.keys())
	for string in l:
		loadData(G,string)
	print len(G)
	fh=open("EdgeList.txt",'wb')
	nx.write_edgelist(G, fh)
if __name__ == "__main__": 
	main()
