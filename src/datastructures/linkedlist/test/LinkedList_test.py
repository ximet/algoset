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

def test_LinkedListRemoveFirstNode():
    linkedList = LinkedList()
    linkedList.append(1)
    assert linkedList.head.value == 1
    linkedList.remove(1)
    assert linkedList.head == None

def test_LinkedListRemoveSecondValue():
    linkedList = LinkedList()
    linkedList.append(1)
    linkedList.append(2)
    linkedList.remove(2)
    assert linkedList.head.value == 1
    assert linkedList.head.value == linkedList.tail.value