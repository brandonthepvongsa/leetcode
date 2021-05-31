# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}
        for i, x in enumerate(nums):
            difference = target - x
            if difference in mp:
                return [mp[difference], i]
            mp[x] = i
            
        return False # should not occur
        