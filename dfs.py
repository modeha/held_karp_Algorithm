from stack import Stack
from queue import PriorityQueue
from operator import itemgetter, attrgetter
from node_tree import NodeTree
def dfs(g):
    """ 
     Breadth-first search (BFS) begins at a root node and order it by 1 and consider all its neighbors
     nodes. Then order the one of them that has min distance . This procedure repeat for the neighbors 
     of this  node and so on, until it finds the goal.
     """    
    for node in g.get_nodes():
        if not node.is_visited():            
            dfs_visit(g, node)
    return

def dfs_visit(g, root):

    stack = Stack()
    stack.push(root)  # root devient racine d'une nouvelle arborescence.      
    root.set_order(0)
    order = root.get_order()    
    while not stack.is_empty():
        u = stack.pop()
        u.set_visited()        
        order += 1
        u.set_order(order)        
        neighbors= sorted(g.get_neighbors(u), key=attrgetter(attribute(g)), reverse=True) 
        # attrgetter key is nice and fast. In fact attrgetter key is called with a string and returns
        #a function that fetches that attribute.
        while neighbors:            
            v = neighbors.pop(0)            
            if not v.is_visited():               
                stack.push(v)                
    return

def attribute(g):
    ""
    if isinstance(g.get_nodes()[0], NodeTree):
        return '_NodeTree__rank'
    else:
        return '_MarkedNode__order'

if __name__ == '__main__':

    from marked_node import MarkedNode
    from edge import Edge
    from graph import Graph

    g = Graph()

    # This nodes for Prim algorithm
    a = MarkedNode(name='a') # id = 0
    b = MarkedNode(name='b') # id = 1
    c = MarkedNode(name='c') # id = 2
    d = MarkedNode(name='d') # id = 3
    e = MarkedNode(name='e') # id = 4
    f = MarkedNode(name='f') # id = 5
    g = MarkedNode(name='g') # id = 6
    
    
 
    nodes = [a, b, c, d, e, f, g]
    
    g = Graph()
    
    g.add_nodes(nodes)
    
    g.add_edge(Edge(a,d,1))   # arete [a,b]
    g.add_edge(Edge(a,b,3))   # arete [a,h]
    
    g.add_edge(Edge(b,c,80))   # arete [b,c]
    g.add_edge(Edge(a,c,2))   # arete [c,i]
    g.add_edge(Edge(a,e,2))   # arete [c,f]
    g.add_edge(Edge(e,g,7))   # arete [c,d]
    g.add_edge(Edge(e,f,17))
    g.add_edge(Edge(f,g,70))
    from algorithms import Algorithms
    algo=Algorithms()
    MST=algo.prim(g,a)
    #print MST.get_edges()

    #for node in g.get_nodes():
        #print node
    #for property, value in vars(a).iteritems():
            #print property, ": ", value
        
    dfs(MST)
    

    print 'Using dfs on this graph we have :'
    for node in sorted(g.get_nodes(),key=attrgetter('_MarkedNode__order')):
        print (node.get_name(),node.get_order(),node.get_distance())