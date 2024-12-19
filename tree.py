# a full binary tree is one where each node has zero or two children
# a perfect binary tree is one where all interior nodes have two children and all leaves have the same depth
# a complete binary tree is where every level is completely filled and all nodes in the last level are as far left as possible
# a binary search tree is where children higher than the parent are put to the right and children lower than the parent are put to the left

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        if self.root == None:
            return False
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
        return False