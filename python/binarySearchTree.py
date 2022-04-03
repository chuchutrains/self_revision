# Binary Search Tree online guide:
# https://qvault.io/python/binary-search-tree-in-python/

# For reference, ICT1008 Binary Search Tree Lecture Slides:
# https://drive.google.com/drive/u/1/folders/1RqTidPWpd-BMGi0nGNzBxeHrGmzE9op_
# @TODO: Implement delete, count.

class BSTNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    def printBST(self, msg):
        if self.left:
            self.left.printBST(msg)
        if self.value:
            msg.append(self.value)
        if self.right:
            self.right.printBST(msg)
        return msg

    def insert(self, value):
        if self == None:
            self = BSTNode(value)
        elif value < self.value:
            if self.left:
                self.left.insert(value)
                return
            self.left = BSTNode(value)
        elif value > self.value:
            if self.right:
                self.right.insert(value)
                return
            self.right = BSTNode(value)

    def min(self):
        node = self
        while node.left:
            node = node.left
        return node.value

    def max(self):
        node = self
        while node.right:
            node = node.right
        return node.value
    
    def delete(self, value):
        pass

    def find(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left == None:
                return False
            return self.left.find(value)
        elif value > self.value:
            if self.right == None:
                return False
            return self.right.find(value)

# Test insert.
bst = BSTNode(10)
bst.insert(2)
bst.insert(60)
bst.insert(1)
bst.insert(3)
bst.insert(5)
print("=== Test insert ===")
print(bst.printBST([]))
# Test min and max.
print("=== Test min and max ===")
print(bst.min())
print(bst.max())
# Test delete.
# print("=== Test delete ===")
# bst.delete(10)
# bst.delete(2)
# bst.delete(60)
# bst.delete(1)
# bst.delete(3)
# bst.delete(5)
# print(bst.printBST([]))
# Test find.
print("=== Test find ===")
print(bst.find(5))