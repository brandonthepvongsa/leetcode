# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        order_map = {}
        
        for i, char in enumerate(order):
            order_map[char] = i +500
        
        for i, word in enumerate(words):
            if i == len(words) -1:
                continue
            if not self.is_sorted(word, words[i+1], order_map):
                return False
                
        return True
                
    def is_sorted(self, word1, word2, order_map, comparison_index = 0 ):
        ret = False
        
        
        if comparison_index > len(word1) and comparison_index > len(word2):
            return True
        
        if comparison_index < len(word1):
            word1_letter = word1[comparison_index]
            word1_value = order_map[word1_letter] # 0
        else:
            word1_value = 0
            
        if comparison_index < len(word2):
            word2_letter = word2[comparison_index]
            word2_value = order_map[word2_letter] # 0
        else:
            word2_value = 0

        
        if word1_value < word2_value:
            return True
        elif word1_value > word2_value:
            return False
        else:
            return self.is_sorted(word1, word2, order_map, comparison_index +1)
        
        
        
        