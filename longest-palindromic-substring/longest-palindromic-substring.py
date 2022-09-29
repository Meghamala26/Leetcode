class Solution:
    def checkPalindrome(self,s,ind1,ind2):
        while(ind1>=0 and ind2 < len(s) and s[ind1]==s[ind2]):
            ind1-=1
            ind2+=1
        return s[ind1+1:ind2]
    
    def longestPalindrome(self, s: str) -> str:
        maxPal=''
        for i in range(len(s)):
            str1=self.checkPalindrome(s,i,i)
            str2=self.checkPalindrome(s,i,i+1)
            
            if len(str1)>len(str2):
                if len(maxPal)< len(str1):
                    maxPal=str1
            else:
                if len(maxPal)< len(str2):
                    maxPal=str2
                
            
            
                
            
            
        return maxPal
            
        
        
    