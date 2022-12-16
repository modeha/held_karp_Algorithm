from marked_node import MarkedNode
from node_tree import NodeTree
from tsp_to_graph import TspToGraph
from algorithms import Algorithms
import  time
import sys

FileNames=['bayg29.tsp','bays29.tsp','brazil58.tsp','brg180.tsp',
              'dantzig42.tsp','fri26.tsp','gr17.tsp','gr21.tsp','gr24.tsp',
              'gr48.tsp','gr120.tsp','hk48.tsp','swiss42.tsp']#,'pa561.tsp']

for File_name in FileNames:
    
    algo=Algorithms()	
    obj=TspToGraph(FileName=File_name,nodeType=MarkedNode)
    G=obj.tsp_to_graph()
   
    #Fide MST using Prim's alghorithm for given .tsp file.
    root=G.get_node(0)
    start = time.clock()
    MSTprim=algo.prim(G,root)
    elapsed = (time.clock() - start)
    print "Minimum Spanning Tree using Prim's algorithm for %s has  %d weight." \
          %(File_name,MSTprim.get_weight())	
    print "Total time for %s  file is:%f using Prim's algorithm.\n" %(File_name,elapsed)
    
    #Fide MST using kruscal's alghorithm for given .tsp file.
    obj=TspToGraph(FileName=File_name,nodeType=NodeTree)
    G=obj.tsp_to_graph()
    start = time.clock()
    MSTkruskal=algo.kruskal(G)	
    print "Minimum Spanning Tree using using Kruskal's algorithm for %s has  %d weight." \
          %(File_name,MSTkruskal.get_weight())
    elapsed = (time.clock() - start)
    print "Total time for %s  file is:%f using Kruskal's algorithm.\n" %(File_name,elapsed)
    



