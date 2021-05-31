# https://leetcode.com/problems/find-all-the-lonely-nodes/
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ret = []
        
        if root == None:
            return root
        else:
            tree_queue = [root]
            
        while len(tree_queue) > 0:
            
            curr = tree_queue.pop(0)
            
            if curr.left:
                tree_queue.append(curr.left)
            
            if curr.right:
                tree_queue.append(curr.right)
            
            if (curr.left and not curr.right):
                ret.append(curr.left.val)
            elif (curr.right and not curr.left):
                ret.append(curr.right.val)
            
        return ret
            
            
        