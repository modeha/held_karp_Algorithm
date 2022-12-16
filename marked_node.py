from node import Node
class MarkedNode(Node):
    """
    """
    def __init__(self, *args, **kwargs):
        super(MarkedNode, self).__init__(*args, **kwargs)
        self.__parent = None
        self.__visited = False
        self.__distance = float("inf")
        self.__order = 0
    
    def is_visited(self):
            return self.__visited

    def set_visited(self):
        self.__visited = True
        
    def set_order(self, order):
        self.__order = order

    def get_order(self):
        return self.__order

    def get_distance(self):
        "Return the distance that associated."
        return self.__distance

    def set_distance(self, val):
        "Set a distance to the node."
        self.__distance = val

    def set_parent(self, node):
        "Set a parent to the node."
        self.__parent = node
        
    def get_parent(self):
        "Return parent of node."
        return self.__parent
      
    def __lt__(self,other):
            return self.__distance < other.get_distance()
        
    def __gt__(self, other):
        return self.__distance > other.get_distance()
    
    def __repr__(self):
        s = 'Node %s' %self.get_name()
        d = self.get_distance()
        s  += '  has distance %s' %  `d`
        if self.get_parent() != None:
            s += '\n    from parent : %s' %self.get_parent().get_name()
        return s
if __name__ == '__main__':
    
    from markedNode import MarkedNode
    a = MarkedNode(name='a',data=4)
    b = MarkedNode(name='b')
    c = MarkedNode(name='c')
    d = MarkedNode(name='d')
    e = MarkedNode(name='e')
    f = MarkedNode(name='f')
    g = MarkedNode(name='g')
    h = MarkedNode(name='h')
    i = MarkedNode(name='i')
  
    nodes=[a,b,c,d,e,f,g,h,i]
    for node in nodes:
        print node
    print nodes[0].get_data()

            
