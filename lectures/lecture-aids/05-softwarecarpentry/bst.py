class BST(object):
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
                return None
            if self.right:
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
    
    def __init__(self):
        self.root = None

    def add(self,elem):
        if self.root is None:
            self.root = _BinaryElem(elem)
        self.root.add(elem)

    def find(self,elem):
        if self.root is None: return None
        return self.root.find(elem)


def rotatedown(top,elem):
    def rotateleft(top):
        assert top.left is not None
        left = top.left
        A = left.left
        B = left.right
        C = top.right
        top.elem, left.elem = left.elem, top.elem
        top.left = A
        top.right = left
        left.left = B
        left.right = C

    def rotateright(top):
        assert top.right is not None
        right = top.right
        A = top.left
        B = right.left
        C = right.right
        top.elem, right.elem = right.elem,top.elem
        top.left = B
        right.left = A
        right.right = C
    while top.elem != elem:
        if elem < top.elem:
            top = top.left
        else:
            top = top.right
        if top is None:
            return
    while top.left and top.right:
        if top.left:
            rotateleft(top)
            top = top.left
        if top.right:
            rotateright(top)
            top = top.right

def remove(top,elem):
    def removeleaf(top):
        if elem < top.elem:
            if top.left.elem == elem:
                assert top.left.left is None
                assert top.left.right is None
                top.left = None
            else:
                removeleaf(top.left)
        else:
            if top.right == elem:
                assert top.right.right is None
                assert top.right.left is None
                top.right = None
            else:
                removechildless(top.right)
    if top.find(elem) is None:
        return
    top = rotatedown(top,elem)
    removeleaf(top)
