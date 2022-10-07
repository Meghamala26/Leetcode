class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        res=""
        for x in s:
            if x!=']':
                stack.append(x)
            else:
                s=""
                while(stack[-1]!='['):
                     s=stack.pop()+s
                     #print(stack)
                stack.pop()
                num=''
                while(stack and stack[-1].isnumeric()):
                    num=stack.pop()+num
                    
                found=s*int(num)
                if len(stack)==0:
                    res+=found
                else:
                    stack.append(found)
                    
        if len(stack)>0:
            res+="".join(stack)
        
        return res
                