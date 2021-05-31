# https://leetcode.com/problems/cousins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#
#
#      1
#    /   \
#   2     3
#  / \
# null 4

class TreeWalker():
    def __init__(self, tree, x, y):
        self.level1 = None
        self.level2 = None
        
        self.x = x
        self.y = y
        
        self.walk_tree(tree)
        
        res = False
        if (self.level1 and self.level2) and (self.level1 == self.level2):
            res = True
        
        self.cousins = res
    
    def walk_tree(self, tree, level=0):
        if tree == None:
            return
        
        if tree.left and tree.right:
            if (tree.left.val == self.x and tree.right.val == self.y) or (tree.left.val == self.y and tree.right.val == self.x):
                return False
        
        if tree.val == self.x:
            self.level1 = level
        
        if tree.val == self.y:
            self.level2 = level
            
        if tree.left:
            self.walk_tree(tree.left, level + 1)
        
        if tree.right:
            self.walk_tree(tree.right, level + 1)
        

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        walker = TreeWalker(root, x, y)
        
        return walker.cousins
        
        
        # DFS, count levels
        # helper function to find level of an element
        # 1. pop from stack
        # 2. Check level, check value
        # 3. add children to stack
        # walk through tree keep level1, level2 
        
        
        
        