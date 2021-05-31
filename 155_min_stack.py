# https://leetcode.com/problems/min-stack/
class MinStack(object):
    
    def __init__(self):
        self.stack = []
        self.length = 0


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        current_min = 0
        if len(self.stack) == 0:
            current_min = x
        else:
            current_min = self.stack[len(self.stack) -1][1]
            
            if x < current_min:
                current_min = x
    
        
        self.stack.append([x, current_min])
        

    def pop(self):
        """
        :rtype: None
        """
        val = self.stack.pop(-1)[0]
        
        return val
        

    def top(self):
        """
        :rtype: int
        """
        
        return self.stack[self.length - 1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        
        return self.stack[self.length - 1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()