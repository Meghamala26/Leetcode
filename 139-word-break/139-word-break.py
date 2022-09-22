class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        memo=[False]*(len(s)+1) 
        memo[len(s)]=True
        
        def checkWordBreak(s, wordDict,memo):
            
            for i in range(len(s)-1,-1,-1):
                for word in wordDict:
                    if i+len(word)<= len(s) and s[i:i+len(word)]==word:
                        memo[i]=memo[i+len(word)]
                    if memo[i]:
                        break
            return memo[0]
            
            
        
        return checkWordBreak(s,wordDict,memo)
        