# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        curr = root
        
        while curr != None:
            if curr.val == val:
                return curr
            elif curr.val < val and curr.right:
                curr = curr.right
            elif curr.val > val and curr.left:
                curr = curr.left
            else:
                return None
        
        