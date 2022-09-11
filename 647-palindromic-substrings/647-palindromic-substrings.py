class Solution:
    
    
    def expandAroundCenter(self,s, left, right):
            count=0
            
            while(left>=0 and right < len(s) and s[left]==s[right]):
                    left-=1
                    right+=1
                    count+=1
                
            return count
        
    def countSubstrings(self, s: str) -> int:
        
        res=0
        
        for i in range(len(s)):
            res+=self.expandAroundCenter(s,i,i)
            res+=self.expandAroundCenter(s,i,i+1)
        
        
        return res
            
        
        
        
            
        
        