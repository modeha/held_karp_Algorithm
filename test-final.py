from __future__ import division
from held_karp import HeldKarp

from edge import Edge
from node import Node
from marked_node import MarkedNode
from node_tree import NodeTree
from graph import Graph
from tsp_to_graph import TspToGraph
from algorithms import Algorithms
from subgradient import Subgradient
import numpy as np
from copy import copy , deepcopy
from plot import plot


tsp_file_names = ['bayg29.tsp', 'bays29.tsp', 'brazil58.tsp', 'brg180.tsp',
              'dantzig42.tsp', 'fri26.tsp', 'gr17.tsp', 'gr21.tsp', 'gr24.tsp',
              'gr48.tsp', 'gr120.tsp', 'hk48.tsp', 'swiss42.tsp' ]#,'pa561.tsp']
    
file_names= tsp_file_names[1]#'test2.tsp'#
#obj = TspToGraph(file_name=file_names, nodeType=MarkedNode)
obj = TspToGraph(file_name=file_names, nodeType=NodeTree)
g=obj.tsp_to_graph()    
g=deepcopy(g)

#root=g.get_node(1)
#remove=g.get_node(0)
algo=Algorithms()

#hk.update_weight(g,[0,1,2,3])
#for i in range(g.get_nb_nodes()):
#for i in range(g.get_nb_nodes()):
hk=HeldKarp(g,algo, 0, 1)
hk.find_maximum()

#print "NEW ITERATION WITH NEW ROOT %d" %i

#print hk.min_one_tree().get_weight()


#print mst.get_adjacents()
#print mst.get_degree(mst.get_node(1))
 
#hk.update_weight()
#print hk.subgradient()
#x=np.array([2,3,1,1])
#print hk.f(x)
#print g.get_weight()

#print hk.it_is_tour(mst)
#print g.get_edges()
#print g.get_degrees()
#print g.get_node(1)
#print hk.subgradient(g)

