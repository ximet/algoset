import ctypes

class StaticArray:
    def __init__(self, size):
        self.countElement = 0
        self.size = size
        self.array = (self.size * ctypes.py_object)()

    def __len__(self):
        return self.countElement
    
    def __getitem__(self, index):
        if not 0 <= index < self.countElement:
            raise IndexError('invalid index')
        return self.array[index]
    
    def append(self, item):
        if self.countElement == self.size:
            raise IndexError('Index Out of Range Exception')
        self.array[self.countElement] = item
        self.countElement += 1