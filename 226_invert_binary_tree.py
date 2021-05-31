# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        head = root
        
        if root != None:
            tree_queue = [root]
        else:
            return None
        
        while(len(tree_queue) > 0):
            curr = tree_queue.pop(0)
            
            if curr.left:
                tree_queue.append(curr.left)
            
            if curr.right:
                tree_queue.append(curr.right)
            
            # Swap if we have left and right
            old_right = curr.right
            
            curr.right = curr.left
            curr.left = old_right
        
        return head
            
            
            
                