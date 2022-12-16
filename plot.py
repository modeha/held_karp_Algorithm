from read_stsp import plot_graph

def object_to_set_dict(g):
	"For plot MST we need to convert objects to set and dictionary."
	edges = g.get_edges()
	nodes = g.get_nodes()
	edges_set = set()
	for edge in  edges:
		u = edge.get_origin().get_name()
		v = edge.get_end().get_name()
		w = edge.get_weight()
		edges_set.add((u,v,w))
        nodes_dict={}	
	for node in nodes:
		nodes_dict[node.get_name()] = node.get_data()
	return nodes_dict,edges_set

def plot(mst):
	" Plot a MST."
	nodes,edges = object_to_set_dict(mst)
	plot_graph(nodes, mst_edges=edges)

if __name__ == '__main__': 
	
	from algorithms import Algorithms
	from tsp_to_graph import TspToGraph	
	from marked_node import MarkedNode
	from node_tree import NodeTree		
	
	file_names = 'bayg29.tsp'
	
	obj = TspToGraph(file_name=file_names, nodeType=NodeTree)
	g = obj.tsp_to_graph()
	algo = Algorithms()	
	mst= algo.kruskal(g)		
	plot(mst)
