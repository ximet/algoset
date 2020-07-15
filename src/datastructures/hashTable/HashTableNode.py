class HashTableNode:
    def __init__(self, key, value, next = None):
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        return {'key': self.key, 'value':self.value, 'next':self.next}
    
    def __str__(self):
        return 'HashTableNode(key='+str(self.key)+', value='+str(self.value)+', next='+str(self.next)+ ')'