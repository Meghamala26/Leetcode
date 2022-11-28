class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo={}
        
        def breakStr(curStr):
            if curStr=='':
                return True
            
            if curStr in memo:
                return memo[curStr]
            
            curWord=''
            res=False
            for i in range(len(curStr)):
                curWord+=curStr[i]
                if curWord in wordDict and breakStr(curStr[i+1:]):
                    res=True
            
            memo[curStr]=res
            return res
                   
            
            
        
        breakStr(s)
        return memo[s]
            
                    
            
        
            
        
        
        
        
            
        