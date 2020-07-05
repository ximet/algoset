class LinkedListNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __repr__(self):
        return {'value':self.value, 'next':self.next}
    
    def __str__(self):
        return 'LinkedListNode(value='+str(self.value)+', next='+str(self.next)+ ')'