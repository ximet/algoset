from src.datastructures.linkedlist.LinkedList import LinkedList

def edgeComparator (edgeA, edgeB):
    if edgeA.getKey() == edgeB.getKey():
        return 0
    return -1 if edgeA.getKey() < edgeB.getKey() else 1

class Vertex:
    def __init__(self, value):
        if value == None:
            raise AttributeError('Problem with value: value is empty')
        self.value = value
        self.edges = LinkedList()
    
    def addEdge(self, edge):
        self.edges.append(edge)
        return self
    
    # def deleteEdge(self, edge):
        #self.edges.delete(edge)