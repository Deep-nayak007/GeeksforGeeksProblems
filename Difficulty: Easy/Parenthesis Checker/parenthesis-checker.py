class Solution:
    def isBalanced(self, s):
        # code here
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                else:
                    output = stack.pop()
                    
                    if char == ')' and output != '(':
                        return False
                    elif char == ']' and output != '[':
                        return False
                    elif char == '}' and output != '{':
                        return False
                        
        if len(stack) == 0:
            return True
        else:
            return False 

            
        
        
        