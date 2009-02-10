class _BinaryElem(object):
    def __init__(self,elem,right=None,left=None):
        self.elem = elem
        self.left = left
        self.right = right
    def find(self,elem):
        if self.elem == elem:
            return self
        elif elem < self.elem:
            if self.left:
                return self.left.find(elem)
        elif self.right:
            return self.right.find(elem)
        return None
    
    def add(self,elem):
        if self.elem == elem: return
        if elem < self.elem:
            if self.left is None:
                self.left = _BinaryElem(elem,None,None)
            else:
                self.left.add(elem)
        else:
            if self.right is None:
                self.right = _BinaryElem(elem,None,None)
            else:
                self.right.add(elem)
class BinarySearchTree(object):
    '''
    Binary Serch Tree

    Operations:
        * create:
        * BST.add(value)
        * BST.remove(value)
        * BST.find(value)
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

    def remove(self,elem):
        '''
        T.remove(value)

        Remove element from tree
        NOP if element does not exist in tree.
        '''

        def removeleaf(leaf):
            assert leaf.left is None
            assert leaf.right is None
            leafpar = self.root
            while leafpar.left is not leaf and leafpar.right is not leaf:
                if leaf.elem < leafpar.elem:
                    leafpar = leafpar.left
                else:
                    leafpar = leafpar.right
            if leafpar.left is leaf:
                leafpar.left = None
            else:
                leafpar.right = None
        def rotateright(Q):
            assert Q.left is not None
            P = Q.left
            A = P.left
            B = P.right
            C = Q.right
            Q.elem, P.elem = P.elem, Q.elem
            Q.left = A
            Q.right = Q
            P.left = B
            P.right = C

        def rotateleft(P):
            assert P.right is not None
            Q = P.right
            A = P.left
            B = Q.left
            C = Q.right
            P.elem, Q.elem = Q.elem,P.elem
            P.left = Q
            P.right = C
            Q.right = A
            Q.left = B

        def rotatedown(node):
            val = node.elem
            while node.left or node.right:
                assert node.elem == val
                if node.left:
                    rotateright(node)
                    node = node.right
                if node.right:
                    rotateleft(node)
                    node = node.left
            return node

        if self.root is None:
            return
        node = self.root.find(elem)
        assert node.elem == elem
        if node is None:
            return
        node = rotatedown(node)
        removeleaf(node)
        assert not self.find(elem)

