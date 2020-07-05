from src.datastructures.linkedlist.LinkedList import LinkedList

def test_linkedListWithOneNode():
    linkedList = LinkedList()
    linkedList.append(1)

    assert linkedList.head.value == 1

def test_LinkedListWithTwoNode():
    linkedList = LinkedList()
    linkedList.append(1)
    linkedList.append(2)

    assert linkedList.head.value == 1
    assert linkedList.tail.value == 2
