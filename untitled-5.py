from read_stsp import plot_graph
file_name='bayg29.tsp'
from algorithms import Algorithms
from tsp_to_graph import TspToGraph
from edge import Edge
from marked_node import MarkedNode
from node_tree import NodeTree
from queue import PriorityQueue
from graph import Graph
from disjoint_set import DisjointSet
from collections import defaultdict
import sys
import time
def ObjectToSet(G):
	edges=G.get_edges()
	nodes=G.get_nodes()
	Edges=set()
	for edge in  edges:
		u= edge.get_origin_edge().get_name()
		v=edge.get_end_edge().get_name()
		w=edge.get_weight()
		Edges.add((u,v,w))
        Nodes={}
	
	for node in nodes:
		Nodes[node.get_name()]=node.get_data()
	return Edges,Nodes

if __name__ == '__main__':  
	
	obj=TspToGraph(FileName=file_name,nodeType=NodeTree)
	G=obj.tsp_to_graph()
	algo=Algorithms()
	start = time.clock()
	mst_kruskal=algo.kruskal(G)	
	elapsed = (time.clock() - start)
	
	Edges,Nodes=ObjectToSet(mst_kruskal)
	Edges2,Nodes2=ObjectToSet(G)
	
	plot_graph(Nodes,mst_edges=Edges)
