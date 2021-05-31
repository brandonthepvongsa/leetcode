# https://leetcode.com/problems/closest-binary-search-tree-value/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        
        closest = root.val
        
        curr = root
        
        while curr:
            if abs(curr.val - target) < abs(closest - target):
                closest = curr.val
            
            if curr.val > target and curr.left:
                curr = curr.left
            elif curr.val < target and curr.right:
                curr = curr.right
            else:
                curr = None
        
        return closest
        