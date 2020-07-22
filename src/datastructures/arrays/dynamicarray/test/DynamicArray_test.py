from src.datastructures.arrays.dynamicarray.DynamicArray import DynamicArray

def test_dynamicArrayCheckAppendAndGetItem():
    array = DynamicArray()
    array.append(1)
    assert array[0] == 1

def test_dynamicArrayCheckCount():
    array = DynamicArray()
    array.append(1)
    array.append(2)
    array.append(3)
    assert array[0] == 1
    assert array[1] == 2
    assert array[2] == 3
    assert len(array) == 3

def test_dynamicArrayCheckResize():
    array = DynamicArray()
    array.append(1)
    array.append(2)
    array.append(3)
    array.append(4)
    array.append(5)
    assert array.capacity == 8