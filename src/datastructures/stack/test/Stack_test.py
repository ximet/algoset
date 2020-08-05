from src.datastructures.stack.Stack import Stack

def test_stackIsEmpty():
    stack = Stack()

    assert stack.isEmpty() == True

def test_stackNotEmpty():
    stack = Stack()
    stack.push(2)

    assert stack.isEmpty() == False

def test_stackPopValue():
    stack = Stack()
    stack.push(2)

    assert stack.pop() == 2
    assert stack.isEmpty() == True

def test_stackPeekValue():
    stack = Stack()
    stack.push(2)

    assert stack.peek() == 2
    assert stack.isEmpty() == False