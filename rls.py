from dfs import dfs
from node import Node
from graph import Graph
from marked_node import MarkedNode
from tsp_to_graph import TspToGraph 
from operator import itemgetter, attrgetter
def rls(tsp_file_name, alghorithm, root_name):
    """
    Approximate Traveling Salesman Algorithms.(Rosenkrantz, Stearns and Lewis).
    PROCEDURE:
    Step 1.  
    Step 2. 
    Step 3. 
    """  
    algo = Algorithms()    
    if alghorithm == 'Prim' or alghorithm == 'prim' :
        obj = TspToGraph(file_name=tsp_file_name, nodeType=MarkedNode)
        g = obj.tsp_to_graph()        
        root = g.get_node(root_name)
        mst = algo.prim(g, root)
        attribute = '_MarkedNode__order'
    elif alghorithm == 'Kruskal' or alghorithm == 'kruskal':
        obj = TspToGraph(file_name=tsp_file_name, nodeType=NodeTree)
        g = obj.tsp_to_graph()   
        mst = algo.kruskal(g)
        attribute = '_NodeTree__rank'
       
    else:
        raise ValueError, "you must select name of alghorithm ."
    dfs(mst)
    
    tour_edges = []
    tour_nodes = sorted(mst.get_nodes(), key=attrgetter(attribute))
    
    for i in range(len(tour_nodes)-1):
        tour_edges.append(g.get_origin_end(tour_nodes[i], tour_nodes[i+1]))
    tour_edges.append(g.get_origin_end(tour_nodes[0], tour_nodes[-1]))
    
    return fill_graph(tour_nodes, tour_edges)

def fill_graph(nodes, edges):
    ""
    g=Graph()    
    for node in nodes:
        g.add_node(node)        
    for edge in edges:
        g.add_edge(edge)    
    return g

if __name__ == '__main__':
    from edge import Edge
    from node_tree import NodeTree
    from algorithms import Algorithms     
    from plot import plot
    import time
    import sys
    tsp_file_names = ['bayg29.tsp', 'bays29.tsp', 'brazil58.tsp', 'brg180.tsp',
              'dantzig42.tsp', 'fri26.tsp', 'gr17.tsp', 'gr21.tsp', 'gr24.tsp',
              'gr48.tsp', 'gr120.tsp', 'hk48.tsp', 'swiss42.tsp' ]#,'pa561.tsp']
    for tsp_file_name in tsp_file_names :
        
        obj = TspToGraph(file_name=tsp_file_name, nodeType=MarkedNode)
        #obj = TspToGraph(file_name=tsp_file_name, nodeType=NodeTree)
        g = obj.tsp_to_graph()
        for i in range(g.get_nb_nodes()):
            #file_names='pa561.tsp'#'pa561.tsp'#sys.argv[1]        
            tour = rls(tsp_file_name, 'prim', i)        
            print "Optimal tour using Prim's algorithm for %s with node %2d is %d ." %(tsp_file_name, i, tour.get_weight())
            
            #print "Total time for %s  file is:%f using Rosenkrantz, Stearns and Lewis algorithm.\n" %(file_names, elapsed)
        plot(tour)
            #start = time.clock() 
            #elapsed = (time.clock() - start)
