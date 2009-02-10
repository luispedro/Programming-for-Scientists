from bst import BinarySearchTree
def test_bst():
    B = BinarySearchTree()
    assert B.size() == 0
    B.add(25)
    assert B.size() == 1
    B.add(25)
    assert B.size() == 1
    B.add(25)
    assert B.size() == 1
    B.add(15)
    assert B.size() == 2
    assert B.find(25)
    assert B.find(15)
    assert not B.find(2)
    B.remove(15)
    assert B.size() == 1
    assert not B.find(15)
    assert B.find(25)
    assert not B.find(2)

