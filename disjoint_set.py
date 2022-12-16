from node_tree import NodeTree

class DisjointSet(object):    
    """
    tree implementation of a disjoint set system utilizing a Node class
    """    
    
    def initialize(self, u):
        """
        Intialize that will be used in the disjoint set system. Each value from values is used to create
        a node that has a parent that is itself.
        """
        u.set_parent(u)
        u.set_rank(0)
        return u
    
    def make_set(self, nodes):
        "Initialize all the node and add them to the tree."
        node_plus = []
        for node in nodes:
            node_plus.append(self.initialize(node)) 
        return node_plus 
            
    def union_rank(self, u, v):        
        """
        Depending on whether the roots of the trees have equal rank. If the roots have unequal rank,
        we make the root with higher rank the parent of the root with lower rank, but the ranks 
	themselves remain unchanged. If, instead, the roots have equalranks, we arbitrarily choose one
        of the roots as the parent and increment its rank.
	"""
        u,v = self.find(u), self.find(v)
        if u.get_rank() > v.get_rank():
            v.set_parent(u)
        else:
            u.set_parent(v)
            if u.get_rank() == v.get_rank():
                v.set_rank( u.get_rank() + 1)
                
    def find(self, u):
        """ 
        Each call of find returns parent[u] in third line. If u is the root, then find skips second
        line and instead returns parent[u], which is u, so in this case the recursion bottoms out.
	Otherwise, second line executes, and the recursive call with parent[u] returns a pointer
        to the root. second Line updates node u to point directly to the root, and the third line returns
        this pointer.
	"""
        if u != u.get_parent():
            u.set_parent( self.find( u.get_parent() ) )
        return u.get_parent()
    
if __name__ == '__main__':
    
    a =  NodeTree(name = 'a')  
    b =  NodeTree(name = 'b')  
    c =  NodeTree(name = 'c')  
    d =  NodeTree(name = 'd')  
    e =  NodeTree(name = 'e')          
    nodes = [a, b, c, d, e]    
    obj = DisjointSet()
    obj.make_set(nodes)    
    a.set_parent(d)
    c.set_parent(a)
    e.set_parent(a)
    obj.union_rank(b, a)    