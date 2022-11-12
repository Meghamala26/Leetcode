class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        sCount=Counter(s) # O(n)
        tCount=Counter(t) # O(n)
        res=0
        
        for ch,freq in tCount.items(): # O(m)
            if ch in sCount:
                if sCount[ch]>=freq:
                    continue
                else:
                    res+=abs(sCount[ch]-freq)
                
            else:
                res+=freq
                
        return res
                    
            
        