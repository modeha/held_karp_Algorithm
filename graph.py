import copy
from collections import defaultdict

class Graph(object):    
    """
    Une classe generique pour representer un graphe comme un ensemble de noeuds.
    """
    
    def __init__(self, name='Sans nom'):
        self.__name = name
        self.__nodes = []  # Liste des objets de classe Node
        self.__edges = []  # Liste des objets de classe Edge
	self.__adjacents = {}		 
    
    def get_name(self):
	"Donne le nom du graphe."
        return self.__name
    
    def add_node(self, node):
        "Ajoute un noeud au graphe."
        self.__nodes.append(node)
    
    def add_list_nodes(self, nodes):
	self.__nodes = nodes
   
    def add_nodes(self):
	"Add a list of nodes to the Graph."
        self.__nodes = self.__adjacents.keys()
    
    def get_nodes(self):
	"Donne la liste des noeuds du graphe."
        return self.__nodes
    
    def get_nb_nodes(self):
        "Donne le nombre de noeuds du graphe."
        return len(self.__nodes)
    
    def get_weight(self, edge):
	"Return the weight of edge"
	return edge.get_weight()
    
    def add_edge(self, edge):
	"Ajoute une arete au graphe."
	self.__edges.append(edge)	
    
    def get_edges(self):
	"Donne la liste des aretes du graphe."
        return self.__edges

    def get_nb_edges(self):
        "Donne le nombre des arretes du graphe."
        return len(self.__edges)

    def get_node(self, name):
        "Return a node with this name."
	for node in self.__nodes:
	    if node.get_name() == name:
		return node
	return None
    
    def set_adjacents(self, d):
	""
	self.__adjacents = d	   
    
    def set_adjacent(self, node, edge):
	""
	if node in self.__adjacents.keys():
	    self.__adjacents[node].append(edge)
	else :
	    self.__adjacents[node]=edge    
	
    def get_adjacents(self):
	""
	return self.__adjacents
    
    def get_neighbors(self,node):
	"Return a list of nodes that related to this node."
	neighbors = []	
	for edge  in self.__adjacents[node]:	    
	    neighbors.append(edge.get_other_vertex(node))
	return neighbors    
	    
    def set_nodes_weight(self, values):
	""
	for node in self.__nodes:
	    node.set_weight(values[node.get_name()])       
    
    def get_origin_end(self, origin, end):
	"Return the edge that have these nodes on both sides."
	adjacents = self.__adjacents[origin]
	for edge in adjacents:
	    if end == edge.get_other_vertex(origin):
		return edge
	            
    def remove_node(self, node):
	"Remove a node and all edges that related to this node."
	tmp=self.__adjacents[node]
	for edge in self.__adjacents[node]:	    
	    self.__edges.remove(edge)
	self.__nodes.remove(node)
	self.__adjacents.__delitem__(node)
	for edge in tmp:
	    for node in self.__adjacents:
		if edge in self.__adjacents[node]:
		    self.__adjacents[node].remove(edge)
    	    
    def get_weight(self):
	"Return the weight of graph."
	weight = 0
	for edge in self.__edges:
	    if  edge != None:
		weight+= edge.get_weight()
	return weight
    
    def get_degree(self, node):
	"Return the degree of a node in the graph."
	if node not in self.__adjacents.keys():
	    return 0
	return len(self.__adjacents[node])
    
    def get_degrees(self):
	"Return a dictionary with key as node and the value as  degree of the node."
	degrees = {}
	for node in self.__adjacents:
	    degrees[node] = len(self.__adjacents[node])
	return degrees
    
    def __repr__(self):
        name = self.get_name()
        nb_nodes = len(self.__nodes)
        nb_edges = len(self.__edges)
        nodes = self.get_nodes()
        s  = 'Graphe %s comprenant %d noeuds' % (name, nb_nodes)
        s += ', et %d aretes:' %nb_edges
	s += '\n Printing Nodes:'
        for node in self.get_nodes():
            s += '\n %s  ' % `node`
        s += '\n Printing Edges:'
        for edge in self.get_edges():
	    s += '\n %s' % `edge`
        return s    

if __name__ == '__main__':
    
    from edge import Edge
    from node import Node
    from marked_node import MarkedNode
    import sys
    from tsp_to_graph import TspToGraph
    import numpy as np
    File_name = 'test.tsp'
    obj =TspToGraph(file_name=File_name, nodeType=MarkedNode)
    g = obj.tsp_to_graph()
    a = g.get_node(0)
    for node in g.get_nodes():
	print node.get_weight()
    g.set_nodes_weight(np.array([-1,-2,-3,-4]))
    for node in g.get_nodes():
	print node.get_weight()