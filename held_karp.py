from __future__ import division

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

import sys
class HeldKarp(object):    
    """
    This class solves the Travelling Salesman Problem
    for a given Graph using the Held-Karp algorithm.
    It finds the optimal Hamiltonian circuit using Prim's and Kruskal
    algorithms. Initially, the Edge with the sum of the two lowest
    Connections is set aside. Then, a Minimum Spanning Tree is found
    with the two points the initial Edge is connected to as the end-points.
    Once an MST has been established, the two unconnected Edges are joined,
    completing the Hamiltonian circuit.
    """
    
    def __init__( self, g, mst_alghorithm, remove_node=Node(), root_node=Node()):
        self.g = g
        self.mst_alghorithm = mst_alghorithm
        self.remove_node = remove_node
        self.root_node = root_node
        self.w = np.zeros( (self.g.get_nb_nodes()) )
        self.x = np.zeros( (self.g.get_nb_nodes()) )
        
        self.min_one_tree_ = Graph
        self.gradient_ = np.ones( self.g.get_nb_nodes() )
    
    def min_one_tree(self):
        """        
        Temporarily remove vertex 'remove_node' (and its edges) and
        find a spanning tree for vertices without this node.
        Then pick add two cheapest edges from vertex remove_node.
        """   
        g = deepcopy(self.g) 
        
        root_node = g.get_node(self.root_node)
        remove_node = g.get_node(self.remove_node)
        
        adjacent_edges = g.get_adjacents()[remove_node]
        
        
        adjacent_edges.sort()                 #Sort edges objects
        
        two_cheapest_edges = adjacent_edges[0:2] 
        
        g.remove_node(remove_node)        
        
        if isinstance(root_node, MarkedNode):
            self.min_one_tree_ = self.mst_alghorithm.prim(g, root_node )
            
        else:
            self.min_one_tree_ = self.mst_alghorithm.kruskal(g) 
        
        self.min_one_tree_.add_edge(two_cheapest_edges[0])        
        self.min_one_tree_.add_edge(two_cheapest_edges[1])
        self.min_one_tree_.set_adjacent(remove_node, two_cheapest_edges)
        for edge in two_cheapest_edges:
            self.min_one_tree_.set_adjacent(edge.get_other_vertex(remove_node), edge)
        self.min_one_tree_.add_node(remove_node)  
        
        return self.min_one_tree_
    
    def update_weight(self):
        " Update weight to each edge by considering the vertex weight."
        self.g.set_nodes_weight(self.w)
        for edge in self.g.get_edges():
            edge.set_weight(edge.get_weight() + edge.get_origin().get_weight()\
                            + edge.get_end().get_weight())
        
    def f(self, minimizer):
        " Return objective function of maximization problem." 
        
        return self.min_one_tree_.get_weight() + self.gradient_.dot(minimizer)
    
    def gradient(self):
        " Return an array subtracting each elements by 2, element are  degrees of nodes."
        
        degrees = self.min_one_tree_.get_degrees()        
        for node in degrees:
            self.gradient_[node.get_name()] = degrees[node]-2
       
    
    def it_is_tour(self):
        " Verify g is a tour or not."
        k=0
        degrees = self.min_one_tree_.get_degrees()        
        for node in degrees:            
            if degrees[node] == 2:
                k+= 1
        #print self.min_one_tree_.get_nb_nodes() == k 
        return self.min_one_tree_.get_nb_nodes() == k  
    
    def step_size(self, previous_grad=0, current_grad=0, a=1, b=2, iter_k=0,f_n=0,f_star=0):
        " Return an step size for update the next iteration."
        #return np.linalg.norm( 0.7*current_grad + 0.3*previous_grad )
        #return a/(b + iter_k)
        #return 0.7/np.linalg.norm( self.gradient_ )
        return ( f_star - f_n )/np.linalg.norm( current_grad )**2
        
    
    def find_maximum(self):
        ""
        
        t = 0.2
        f_n, f_plus = -float("inf"), 0
        iteration = 0
        self.min_one_tree()
        #self.gradient_ = np.finfo(float).eps
        previous_grad, current_grad = self.gradient_, self.gradient_
        it_is_tour_ = False 
         
        while iteration <20 and  np.linalg.norm( self.gradient_ ) > 1 and  not it_is_tour_ :
            
            #plot(self.min_one_tree_)
            iteration+= 1
            self.update_weight()
            self.min_one_tree()            
            self.gradient()
            self.is_it_ = self.it_is_tour()
            #print max( abs( self.gradient_ ) )             
                      
            #print self.f(self.x)           
            self.x+= t*self.gradient_
            f_n = self.f(self.x) 
            print " %-10f , %-10f " %(f_plus, np.linalg.norm( self.gradient_ ))
            f_plus = max(f_plus, f_n)
            
            #print np.linalg.norm( self.x )
            #print  max( abs( self.x ) )
            #print self.x.shape
            previous_grad = current_grad
            current_grad = self.gradient_
            t = self.step_size(previous_grad, current_grad, iter_k=iteration, f_n=f_plus, f_star=1610)
            self.w = self.x
            it_is_tour_ = self.it_is_tour()
            
            
        #plot(self.min_one_tree_)
            
    
    
if __name__ == '__main__': 
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
    for i in range(g.get_nb_nodes()):
        hk=HeldKarp(g,algo, i, 1)
        hk.find_maximum()
        
        print "NEW ITERATION WITH NEW ROOT %d" %i
    
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
   
