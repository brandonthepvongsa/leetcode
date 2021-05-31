# https://leetcode.com/problems/length-of-last-word/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        
        if len(words) > 0:
            last_word = words[-1]
            return len(last_word)
        else:
            return 0
        