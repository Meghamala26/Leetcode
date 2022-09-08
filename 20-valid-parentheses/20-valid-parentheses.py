class Solution:
    def isValid(self, s: str) -> bool:
        
        brackets= {'(':')', '{': '}', '[': ']'}
        
        stack=[]
        
        for x in s:
            if x == '(' or x=='{' or x=='[':
                stack.append(x)
            else:
                if len(stack)!=0 and brackets[stack[-1]]==x:
                    stack.pop(-1)
                else:
                    return False
        
        if len(stack) ==0:
            return True
        else:
            return False