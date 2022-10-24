class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        sCount=Counter(s)
        tCount=Counter(t)
        res=0
        
        for ch,freq in tCount.items():
            if ch in sCount:
                if sCount[ch]==freq:
                    continue
                elif sCount[ch]<freq:
                    res+=abs(sCount[ch]-freq)
                else:
                    continue
            else:
                res+=freq
                
        return res
                    
            
        