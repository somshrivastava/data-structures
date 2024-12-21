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
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
        
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def minimum_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def r__delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node = self.r__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node = self.r__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.right
            else:
                minimum_value = self.minimum_value(current_node.right)
                current_node.value = minimum_value
                current_node.right = self.r__delete_node(current_node.right, minimum_value)
        return current_node

    def r_delete_node(self, value):
        self.r__delete_node(self.root, value)