from node import Node
from edge import Edge
from node_tree import NodeTree
from marked_node import MarkedNode
from graph import Graph
import sys
import read_stsp as rs
from collections import defaultdict
class TspToGraph():
    "Create a graph object from .tsp file."
    
    
    def __init__(self, nodesObjects=[], g=Graph(), file_name=None, nodeType=None):
	self.__nodesObjects = nodesObjects
	self.g = g
	self.Nodes = {}
	self.nodeType = nodeType
	self.file_name = file_name
	self.obj=Node
	
    def tsp_to_graph(self):
	"Reads a TSP file and return a graph object."
	
	self.set_empty()	
    
	if self.nodeType == None:
	    self.obj = Node
		    
	elif self.nodeType == NodeTree:
	    self.obj = NodeTree
		    
	elif self.nodeType == MarkedNode:
	    self.obj = MarkedNode
	    
	with open(self.file_name, "r") as fd:
	    header = rs.read_header(fd)
	    header = rs.read_header(fd)        
	    nodes = rs.read_nodes(header,fd) 
	    edges = rs.read_edges(header,fd)
	    tmp = {}
	    d = {}
	    for node in nodes:
		vertex = self.obj(name=node, data=nodes[node])
		self.g.add_node(vertex)
		tmp[node] = vertex
	    
	    for u,v,w in edges:
		if tmp[u] != tmp[v]:		    
		    edge = Edge(tmp[u], tmp[v],w)
		    self.g.add_edge(edge)		
		    d.setdefault(tmp[u], []).append(edge)
		    d.setdefault(tmp[v], []).append(edge)
	    self.g.set_adjacents(d)
	    #self.g.add_nodes()
	    return self.g   
	
    def set_empty(self):
	"Set nodes and edges be empty list if we want to use several time this class."
	self.__nodesObjects = []
	self.g = Graph()

if __name__=="__main__":
    
    import sys
    #FileName=sys.argv[1]
    #obj=TspToGraph()
    #g=obj.tspToGraph(FileName,NodeTree)
    #print g.get_nodes()[0]
    import  time	
    file_names = 'test.tsp'
    obj2 = TspToGraph(file_name=file_names, nodeType=MarkedNode)
    start = time.clock()
    g=obj2.tsp_to_graph()
    elapsed = (time.clock() - start)
    print "Total time for %s  file is:%f.\n" %(file_names, elapsed)
    
    #g.get_adjacents()
    
    print g.get_nb_nodes()
    
    
