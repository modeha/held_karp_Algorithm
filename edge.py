from node import Node
class Edge(object):     
     """
     Represents an edge in a graph.
     """     
     __edge_count = [-1]   # Compteur global partage par toutes les instances.
     
     def __init__(self, origin_edge=Node(), end_edge=Node(), weight=0):
          "Constructs an edgebetween the given vertices and with the given weight."
          self.__origin_edge = origin_edge # Objet noeud origine de l'arete.
          self.__end_edge = end_edge       # Objet extremite de l'arete.
          self.__weight = weight
          self.__class__.__edge_count[0] += 1
          self.__id = self.__class__.__edge_count[0]
                    
     def get_id(self):
          "Returns id of Edge."
          return self.__id
     
     def get_origin(self):
          "Returns the first vertex of this edge."
          return self.__origin_edge
      
     def get_end(self):
          "Returns the second vertex of this edge."
          return self.__end_edge
     
     def get_weight(self):
          "Returns the weight of this edge."
          return self.__weight
     
     def set_weight(self, value):
          "Set a new value to the edge."
          self.__weight = value    
     
     def get_other_vertex(self, this_vertex):
          "Get one of the vertex of an edge and return the another one."
          if  this_vertex == self.__end_edge:
               return self.__origin_edge
          elif this_vertex == self.__origin_edge:
               return self.__end_edge
          
     def __eq__(self, other):          
          if self is other : return True
          if type(self) != type(other):
               return False
          return self.__origin_edge == other.__origin_edge and \
                 self.__end_edge == other.__end_edge
     
     def __lt__(self, other):
          return self.__weight < other.__weight

     def __le__(self, other):
          return self.__weight <= other.__weight

     def __gt__(self, other):
          return self.__weight > other.__weight
     
     def __ge__(self, other):
          return self.__weight <= other.__weight
     
     def __repr__(self):
          "Returns the string representation of this edge."
          origin_edge = self.get_origin().get_name()
          end_edge = self.get_end().get_name()
          weight = self.get_weight()
          s  = "Edge [%s,%s]" % (origin_edge, end_edge)
          s += ',has the  weight %d' % weight
          return s


if __name__ == '__main__':
     
     
     
     a = Node(name='a')
     b = Node(name='b')
     c = Node(name='c')
     d = Node(name='d')
     e = Node(name='e')
     f = Node(name='f')
     g = Node(name='g')
     h = Node(name='h')
     i = Node(name='i')
    
     edges = []
    
     edges.append(Edge(a,b,4))
     edges.append(Edge(a,h,8))
     edges.append(Edge(b,h,11))
     edges.append(Edge(b,c,8))
     edges.append(Edge(c,i,2))
     edges.append(Edge(c,f,4))
     edges.append(Edge(c,d,7))
     edges.append(Edge(d,f,14))
     edges.append(Edge(d,e,9))
     edges.append(Edge(e,f,10))
     edges.append(Edge(f,g,2))
     edges.append(Edge(g,i,6))
     edges.append(Edge(g,h,1))
     edges.append(Edge(h,i,7))
     print edges[0].get_weight()
     edges[0].set_weight(23)
     print edges[0].get_weight()
     
