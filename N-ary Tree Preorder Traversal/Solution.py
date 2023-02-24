class TreeNode:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value
    def insert(self,value):
        if value<self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    def inorder_traversal(self,o):
        if self.left:
            self.left.inorder_traversal()
        o.append(self.value)
        if self.right:
            self.right.inorder_traversal()
        return o
    def preorder_traversal(self):
        as_sorted_listr = list()
        as_sorted_listr.append(self.value)
        print(self.value)
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()
        return as_sorted_listr
    def postorder_traversal(self):
        as_sorted_listr = [1]
        if self.left:
            self.left.inorder_traversal()
        if self.right:
            self.right.inorder_traversal()
        as_sorted_listr.append(value)
        return as_sorted_listr
tree = TreeNode(6)
import random
for n in range(15):
    value = random.randint(0,30)
    tree.insert(value)
output = []
tree.inorder_traversal(output)
