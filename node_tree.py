from node import Node
class NodeTree(Node):    
    """
    NodeTree class is used to create each tree. Trees are utilized to structure each set. 
    A node has its own data, a parent node, and a rank.
    """    
    
    def __init__(self,*args, **kwargs):
	super(NodeTree,self).__init__(*args, **kwargs)
	self.__parent = None  
	self.__rank = 0
	self.__order = 0
	self.__visited = False
	
    def is_visited(self):
            return self.__visited

    def set_visited(self):
        self.__visited = True
	
    def set_order(self, order):
        self.__order = order

    def get_order(self):
        return self.__order
    
    def set_rank(self, rank):
	self.__rank = rank
	
    def get_rank(self):
	return self.__rank
    
    def set_parent(self, parent):
	self.__parent = parent   	
	
    def get_parent(self):
	return self.__parent
    
    def __lt__(self, other):
	return self.__rank< other.__rank

    def __le__(self, other):
	return self.__rank<= other.__rank

    def __gt__(self, other):
	return self.__rank > other.__rank
    
    def __ge__(self, other):
	return self.__rank <= other.__rank
    
    def __neq__(self,other):
	return self.rank != other.__rank
    
    def __repr__(self):
        s = 'Node %s' %self.get_name()
        r = self.get_rank()
        s  += '  has rank %s' %  `r`
        #s += '\n   from parent ' + `self.__parent`
        if self.get_parent() != None:
            s += '\n    from parent : %s' %self.get_parent().get_name()
        return s
    
    

if __name__ == '__main__':

    a = NodeTree(name = 'a') 
    b = NodeTree(name = 'b') 
    c = NodeTree(name = 'c') 
    d = NodeTree(name = 'd') 
    a.set_parent(d)
    d.set_parent(c)
    c.set_parent(b)      
    print a 