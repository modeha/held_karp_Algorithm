from edge import Edge
from marked_node import MarkedNode
from node_tree import NodeTree
from queue import PriorityQueue
from graph import Graph
from disjoint_set import DisjointSet
from collections import defaultdict
import sys
import time
class Algorithms(object):
    " Contains a bunch of algorithm like Prim and Kruskal."
    
    def prim(self,g,s):	
	"""
	Uses Prim's Algorithm to produce a minimal spanning tree of weighted graph G.
	The algorithm will start with vertex s.
        """	
	PQ=PriorityQueue()	
	nodes = g.get_nodes()
	s.set_distance(0)	
	for node in nodes:
		PQ.enqueue(node)
	# Now the question is how to find the light edge quickly?
        # The answer is using priority queue.
	start = time.clock()
	while not PQ.is_empty():
		u= PQ.dequeue()	 #returns the smallest item from the PQ.				
		for edge  in g.get_adjacents()[u]:
			weight = edge.get_weight()
			v = edge.get_other_vertex(u)
			if v in PQ and weight<v.get_distance():
				v.set_parent(u)	
				v.set_distance(weight)				
       
        Tree=Graph(name='mst')
	d={}
	Tree.add_node(s)
	for node in nodes:
	    if  node.get_parent() is not None:
		Tree.add_node(node)
		edge = Edge(node, node.get_parent(), node.get_distance())
		Tree.add_edge(edge)
		d.setdefault(node,[]).append(edge)
		d.setdefault(node.get_parent(),[]).append(edge)
	Tree.set_adjacents(d)
	return Tree
    
    def kruskal(self, g):
	"""
	Kruskal's algorithm is an algorithm in graph theory that finds a MST for 
	a connected weighted graph. This means it finds a subset of the edges that forms 
	a tree that includes every vertex, where the total weight of all the edges in the tree
	is minimized. If the graph is not connected, then it finds a minimum spanning forest 
	(a minimum spanning tree for each connected component).
	"""
	obj = DisjointSet()
	mst  = Graph()
	edges = g.get_edges()
	nodes = obj.make_set(g.get_nodes())
	d={}
	for edge in sorted(edges): #we need sort edges by the weights.
		u, v, w = edge.get_origin(), edge.get_end(), edge.get_weight()
	        if obj.find(u) != obj.find(v):
			mst.add_edge(edge)
			d.setdefault(u,[]).append(edge)
			d.setdefault(v,[]).append(edge)
	        	obj.union_rank(u,v)
	mst.set_adjacents(d)
	#mst.add_nodes()
	mst.add_list_nodes(g.get_nodes())
	#print mst
	return mst 

def __prim_test():
	"""
	Note that like kruskal, the prim function here assumes that the graph G is
	an undirected graph.
	"""
	from some_graph import laboratory
	algo=Algorithms()
	g=laboratory(MarkedNode)
	a=g.get_node('h')
	mst_prim=algo.prim(g,a)
	print "Weight of course example  using Prim's algorithm is:%d.\n" % mst_prim.get_weight()
	
def __kruskal_test():
    " kruskal, test for course example."
    from some_graph import laboratory
    algo=Algorithms()
    g=laboratory(NodeTree)
    MST=algo.kruskal(g)
    print "Weight of course example using Kruskal's algorithm is:%d.\n" % MST.get_weight()
    
def __tsp_kruskal(file_names):
    " Finde MST using kruscal's alghorithm for given .tsp file."
    from tsp_to_graph import TspToGraph
    obj = TspToGraph(file_name=file_names, nodeType=NodeTree)
    g = obj.tsp_to_graph()
    algo = Algorithms()
    start = time.clock()
    mst_kruskal = algo.kruskal(g)	
    elapsed = (time.clock() - start)
    print "Minimum Spanning Tree using using Kruskal's algorithm for %s has  %d weight." \
          %(file_names, mst_kruskal.get_weight())
    print "Total time for %s  file is:%f using Kruskal's algorithm.\n" %(file_names, elapsed)
    #print mst_kruskal.get_adjacents()
    print mst_kruskal.get_degree( g.get_node(3) )
    
def __tsp_prim(file_names):
    " Finde MST using Prim's alghorithm for given .tsp file."
    from tsp_to_graph import TspToGraph
    obj = TspToGraph(file_name=file_names, nodeType=MarkedNode)
    g = obj.tsp_to_graph()
    algo = Algorithms()
    root = g.get_node(0)
    start = time.clock()
    
    mst_prim = algo.prim(g, root)
    elapsed = (time.clock() - start)
    print "Minimum Spanning Tree using Prim's algorithm for %s has %d weight." \
          %(file_names, mst_prim.get_weight())	
    print "Total time for %s  file is:%f using Prim's algorithm.\n" %(file_names, elapsed)
    #print mst_prim.get_adjacents()
    #from set_list import intersect
    #e=MSTprim.get_adjacents()
    #nodes=MSTprim.get_nodes()
    #print len(nodes)
    
	

    
    

    
	
if __name__ == '__main__':
	import  time	
	import sys		
	file_names='bayg29.tsp'#'pa561.tsp'##sys.argv[1]	
	#__prim_test()     # This run the course example
	#__kruskal_test()
	__tsp_prim(file_names)	
	__tsp_kruskal(file_names)
	
	


    
    
