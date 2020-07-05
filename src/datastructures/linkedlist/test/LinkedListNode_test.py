from src.datastructures.linkedlist.LinkedListNode import LinkedListNode

def test_linkedListNodeWithoutLink():
    node = LinkedListNode(1)

    assert node.value == 1
    assert node.next == None

def test_2linkedListNodeWithValue():
    node2 = LinkedListNode(2)
    node1 = LinkedListNode(1, node2)
    assert node2.value == 2
    assert node2.next == None
    assert node1.value == 1
    assert node1.next == node2

def test_stringPresentation():
    node = LinkedListNode(1)

    assert str(node) == 'LinkedListNode(value=1, next=None)'