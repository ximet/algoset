from src.datastructures.hashTable.HashTableNode import HashTableNode

def test_linkedListNodeWithoutLink():
    node = HashTableNode(1, 2)

    assert node.key == 1
    assert node.value == 2
    assert node.next == None

def test_stringPresentation():
    node = HashTableNode(1, 2)

    assert str(node) == 'HashTableNode(key=1, value=2, next=None)'