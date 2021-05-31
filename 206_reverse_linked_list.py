# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        front = head
        
        curr = head
        prev = None
        
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        
        return prev
                
                