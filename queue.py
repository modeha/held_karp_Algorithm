class Queue:
    "Une implementation de la structure de donnees << file >>."

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        "Ajoute `item` a la fin de la file."
        self.items.append(item)

    def dequeue(self):
        "Retire l'objet du debut de la file."
        return self.items.pop(0)

    def is_empty(self):
        "Verifie si la file est vide."
        return (len(self.items) == 0)
    
    def __contains__(self,item):
        "This method to allow efficient use of the 'in' operator"
        return item in self.items

    def __repr__(self):
        return `self.items`



class PriorityQueue(Queue):

    def dequeue(self):
        "Retire l'objet ayant la plus petit priorite."
        smallest = self.items[0]
        for item in self.items[1:]:
            if item < smallest:
                smallest = item
        idx = self.items.index(smallest)
        return self.items.pop(idx)
