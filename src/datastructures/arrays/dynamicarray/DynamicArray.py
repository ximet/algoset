import ctypes

class DynamicArray:
    def __init__(self):
        self.countElement = 0
        self.capacity = 1
        self.array = self.createArray(self.capacity)
    
    def createArray(self, size):
        return (size * ctypes.py_object)()

    def __len__(self):
        return self.countElement
    
    def __getitem__(self, index):
        if not 0 <= index < self.countElement:
            raise IndexError('invalid index')
        return self.array[index]

    def resize(self, size):
        tempArray = self.createArray(size)
        for item in range(len(self.array)):
            tempArray[item] = self.array[item]
        self.array = tempArray
        self.capacity = size
    
    def append(self, item):
        if self.countElement == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.countElement] = item
        self.countElement += 1