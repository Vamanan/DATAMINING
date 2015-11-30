import community
import networkx as nx
import sys
import random

import matplotlib.pyplot as plt

ipfile=sys.argv[1]
img=sys.argv[2]

g=nx.Graph()

#read file and construct graph

with open(ipfile) as f:
 for line in f:
  l=line.split()
  g.add_edge(int(l[0]),int(l[1]), weight=1)

opgraph=g.copy()
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




