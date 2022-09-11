class Solution:
    
    
    def expandAroundCenter(self,s, left, right, found):
            count=0
            
            while(left>=0 and right < len(s) and s[left]==s[right]):
                tmp=str(left)+','+str(right)
                if tmp not in found:
                    found.add(tmp)
                    left-=1
                    right+=1
                    count+=1
                else:
                    break
                
            return count
        
    def countSubstrings(self, s: str) -> int:
        
        found=set()
        res=0
        
        for i in range(len(s)):
            res+=self.expandAroundCenter(s,i,i, found)
            res+=self.expandAroundCenter(s,i,i+1, found)
        
        
        return res
            
        
        
        
            
        
        