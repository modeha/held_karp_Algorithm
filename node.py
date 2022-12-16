class Node(object):
    """
    Une classe generique pour representer les noeuds d'un graphe.
    """

    __node_count = [-1]   # Compteur global partage par toutes les instances.

    def __init__(self, name='without name', data=0, weight=0):
        self.__name = name
        self.__data = data
        self.__weight = weight
        self.__class__.__node_count[0] += 1
        self.__id = self.__class__.__node_count[0]
                
    def get_name(self):
        "Donne le nom du noeud."
        return self.__name

    def get_id(self):
        "Donne le numero d'identification du noeud."
        return self.__id
    
    def get_data(self):
        "Donne les donnees contenues dans le noeud."
        return self.__data
    
    def get_weight(self):
        "Return vertex weight."
        return self.__weight
    
    def set_weight(self,value):
        "Set a value to vertex weight of the node."
        self.__weight = value
    
    
    def __eq__(self, other):
        return self.__name == other.get_name()    
    
    def __repr__(self):
        id = self.get_id()
        name = self.get_name()
        data = self.get_data()
        s  = 'Node %s (id %d)' % (name, id)
        s += ' (data: ' + `data` + ')'
        return s


if __name__ == '__main__':

    from node import Node
    a = Node(name='a')
    b = Node(name='b')
    c = Node(name='c')
    d = Node(name='d')
    e = Node(name='e')
    f = Node(name='f')
    g = Node(name='g')
    h = Node(name='h')
    i = Node(name='i')
    a.set_weight(5)
  
    nodes=[a,b,c,d,e,f,g,h,i]
    for node in nodes:
        print node.get_id() ,node.get_name(), node.get_weight()
