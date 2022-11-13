# https://leetcode.com/problems/binary-tree-paths/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        self.path(root, '', res)
        return res
        
    def path(self, root, string, res):
        string += str(root.val)
        if root.left:
            self.path(root.left, string+'->', res)
        if root.right:
            self.path(root.right, string+'->', res)
        if not root.left and not root.right:
            res.append(string)
        