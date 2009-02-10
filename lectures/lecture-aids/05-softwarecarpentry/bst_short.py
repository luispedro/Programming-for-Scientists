class _BinaryElem(object):
    def __init__(self,elem,right=None,left=None):
        self.elem = elem
        self.left = left
        self.right = right
    def find(self,elem):
        if self.elem == elem: return self
        elif elem < self.elem:
            if self.left: return self.left.find(elem)
        elif self.right:  return self.right.find(elem)
        return None 
    def add(self,elem):
        if self.elem == elem: return
        if elem < self.elem:
            if self.left is None: self.left = _BinaryElem(elem,None,None)
            else: self.left.add(elem)
        else:
            if self.right is None: self.right = _BinaryElem(elem,None,None)
            else: self.right.add(elem)
class BinarySearchTree(object):
    '''
    Binary Serch Tree
    Operations:
        * BST.add(value)
        * BST.remove(value)
        * BST.find(value)
	* BST.size()
    '''
    def __init__(self):
        self.root = None
    def add(self,elem):
        '''
        T.add(value)
        Add element to the tree
        '''
        if self.root is None:
            self.root = _BinaryElem(elem)
        self.root.add(elem)
    def find(self,elem):
        '''
        N = T.find(value)
        Returns whether element is in the tree.
        '''
        if self.root is None: return False
        return self.root.find(elem) is not None
    def size(self):
        '''
        N = T.size()
        Return the number of elements in the tree.
        '''
        def _size(top):
            if top is None: return 0
            return 1 + _size(top.left) + _size(top.right)
        return _size(self.root)
