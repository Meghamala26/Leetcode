class Solution:
    def numDecodings(self, s: str) -> int:
        memo={}
        def decode(index):
            if index==len(s):
                return 1
            if s[index]=='0':
                memo[index]=0
                return 0
            if index==len(s)-1:
                return 1
            if index in memo:
                return memo[index]
            
            ans=decode(index+1)
            if int(s[index:index+2])<=26:
                ans+=decode(index+2)
            
            memo[index]=ans
            return ans
        
        return decode(0)
            
            
        