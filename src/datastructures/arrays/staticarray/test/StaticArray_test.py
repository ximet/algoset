import pytest

from src.datastructures.arrays.staticarray.StaticArray import StaticArray

def test_staticArrayCheckAppendAndGetItem():
    array = StaticArray(1)
    array.append(1)
    assert array[0] == 1
    assert len(array) == 1

def test_staticArrayCheckErrorAppend():
    with pytest.raises(IndexError) as excinfo:
        array = StaticArray(1)
        array.append(1)
        array.append(2)
    assert 'Index Out of Range Exception' in str(excinfo.value)

def test_staticArrayProblemWithIndex():
    with pytest.raises(IndexError) as excinfo:
        array = StaticArray(1)
        array.append(1)
        elem = array[4]
    assert 'invalid index' in str(excinfo.value)