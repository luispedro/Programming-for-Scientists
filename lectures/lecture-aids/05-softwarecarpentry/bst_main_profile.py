from bst import BinarySearchTree
import profile

B = BinarySearchTree()
B.add(1)
B.add(3)
B.add(4)

profile.run('B.remove(3)')

