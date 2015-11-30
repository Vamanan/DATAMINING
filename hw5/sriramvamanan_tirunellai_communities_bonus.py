import community
import networkx as nx
import sys
import random

import matplotlib.pyplot as plt


#read file and construct graph

def loadGraph():
 with open(ipfile) as f:
  for line in f:
   l=line.split()
   g.add_edge(int(l[0]),int(l[1]), weight=1)


def getadjlist(g):
 adjlist={}
 for edge in nx.edges(g):
  print edge
  if edge[0] in adjlist:
   adjlist[edge[0]].append(edge[1])
  else:
   adjlist[edge[0]]=[edge[1]]
 return adjlist




def betweenness(g):
 #create adjacency list
 adjlist=getadjlist(g)
 print adjlist
 
 
 #begin bfs; create num shortest paths dict;create bfs tree
 for node in nx.nodes(g):
  bfstree={}
  q=[]
  spdict={}
  splendict={node:0}
  visited=[node]
  q.append(node)
  while len(q)!=0:
   head=q.pop(0)
   for child in adjlist[q]:
    q.append(child)
    if head in bfstree:
     bfstree[head].append(child)
    else:
     bfstree[head]=[child]
    if child not in visited:
     spdict[child]=1 #no of shortest paths to child is 1 
     visited.append(child) 
     splendict[child]=splendict[head]+1 #length of shortest path to child is 1+parent
    elif child in visited:
     if splendict[child]>splendict[head]+1: #we have found a shorter path
      splendict[child]=splendict[head]+1
      spdict[child]=spdict[head]
     elif splendict[child]=splendict[head]+1:
      spdict[child]+=spdict[head]
  #bfs complete
  leafnodes=list(set(nx.nodes(g))-set(bfstree.keys()))
   
    
    
   
  
  
  
  
 
def partition():
 best_modularity=float("-inf")
 best_partition={}

 while(True):
  d=nx.edge_betweenness_centrality(g)
  sorted_edges=sorted(d,key=d.get, reverse=True)
  g.remove_edge(*sorted_edges[0])

  if len(nx.edges(g))==0:
   break
  partition={}
  for c in nx.connected_component_subgraphs(g):
   for node in nx.nodes(c):
    partition[node]=c
  modularity=community.modularity(partition,g)
  if modularity>best_modularity:
   best_modularity=modularity
   best_partition=partition
   best_graph=g.copy()
  
 
 op=[]


 for c in nx.connected_component_subgraphs(best_graph):
  l=[int(x) for x in nx.nodes(c)]
  l.sort()
  op.append(l)

 op.sort(key=lambda x:x[0])
 for x in op:
  print x

 colormap=[]
 seen=[]
 color=5
 for l in op:
  
  for x in l:
   colormap.append(color)
  color+=10


 nx.draw_networkx(opgraph, node_color=colormap)

 plt.savefig(img)



ipfile=sys.argv[1]
img=sys.argv[2]

g=nx.Graph()

loadGraph()
opgraph=g.copy()
partition()
betweenness(opgraph)





