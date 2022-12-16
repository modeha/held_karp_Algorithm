from node import Node
from edge import Edge
from graph import Graph
from marked_node import MarkedNode
from node_tree import NodeTree

def laboratory(node=None):	
	if node==None:
		obj=Node
	elif node==MarkedNode:
		obj=MarkedNode
	elif node==NodeTree:
		obj=NodeTree
		
	"Puts Example of laboratory: in the graph object"
	
	G = Graph(name='laboratory')
	 
	a = obj(name='a')
	b = obj(name='b')
	c = obj(name='c')
	d = obj(name='d')
	e = obj(name='e')
	f = obj(name='f')
	g = obj(name='g')
	h = obj(name='h')
	i = obj(name='i')
	
	nodes = [a, b, c, d, e, f, g, h, i]
	for node in nodes:
		G.add_node(node)
	# Add the edges to the graph object
	
	G.add_edge(Edge(a,b,4))   
	G.add_edge(Edge(a,h,8))   
	G.add_edge(Edge(b,h,11))  
	G.add_edge(Edge(b,c,8))   
	G.add_edge(Edge(c,i,2))   
	G.add_edge(Edge(c,f,4))   
	G.add_edge(Edge(c,d,7))   
	G.add_edge(Edge(d,f,14))  
	G.add_edge(Edge(d,e,9))   
	G.add_edge(Edge(e,f,10))  
	G.add_edge(Edge(f,g,2))   
	G.add_edge(Edge(g,i,6))   
	G.add_edge(Edge(g,h,1))   
	G.add_edge(Edge(h,i,7))   
	return G
    
    
