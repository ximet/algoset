from src.datastructures.linkedlist.LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.stack = LinkedList()
    
    def isEmpty(self):
        return self.stack.head == None

    def push(self, value):
        self.stack.prepend(value)
    
    def pop(self):
        removedItem = self.stack.deleteHead()
        if removedItem == None:
            return None
        return removedItem.value
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.stack.head.value