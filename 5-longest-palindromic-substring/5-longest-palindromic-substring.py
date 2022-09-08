class Solution:
    
    def expandAroundCenter(self, s: str,left: int, right: int) -> str:
        
        while (left>=0 and right < len(s) and s[left]==s[right]):
            left-=1
            right+=1
            
        return s[left+1:right]
    
    def longestPalindrome(self, s: str) -> str:
        
        if len(s)<=1:
            return s
        
        
        res=''
        maxStr=''
        for i in range(len(s)):
            str1=self.expandAroundCenter(s,i,i)
            str2=self.expandAroundCenter(s,i,i+1)
            if len(str1)>len(str2):
                maxStr=str1
                
            else:
                maxStr=str2
                
            
            if len(res)<len(maxStr):
                res=maxStr
            
            
            
            
        return res
    
    
    
    
    
        