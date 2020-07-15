from src.datastructures.hashTable.HashTableNode import HashTableNode

defaultSize = 32

class HashMap:
    def __init__(self, size = defaultSize):
        self.buckets = [HashTableNode] * size

    def hash(self, key):
        return hash(key)
    
    def set(self, key, value):
        keyHash = self.hash(key)