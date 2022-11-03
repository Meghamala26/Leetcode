class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        
        memo=collections.defaultdict(list)
        
        def create(s):
            
            if len(s)==0:
                return [" "]
            if s in memo:
                return memo[s]
            word=""
            for i in range(len(s)):
                word+=s[i]
                if word in wordDict:
                    print(s)
                    stncList=create(s[i+1:])
                    for x in stncList:
                        memo[s].append((word+" "+ x).strip())
                    
                        
            
            return memo[s]
            
                
                
        
        
        
        
        create(s)
        print(memo)
        return memo[s]