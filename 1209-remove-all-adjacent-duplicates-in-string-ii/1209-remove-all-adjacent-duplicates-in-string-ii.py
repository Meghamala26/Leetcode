class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack=[]
        stack.append([s[0],1])
        
        for x in s[1:]:
            if stack and stack[-1][0]==x:
                stack[-1][1]+=1
            else:
                stack.append([x,1])
            
            if stack[-1][1]==k:
                stack.pop()
        
      
        return "".join(x[0]*x[1] for x in stack)
                
                    
                