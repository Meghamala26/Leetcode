class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        res=[]
        
        def create(s,curStnc):
            if len(s)==0:
                res.append(curStnc.strip())
                return 
            word=''
            for i in range(len(s)):
                word+=s[i]
                if word in wordDict:
                    create(s[i+1:], curStnc+word+" ")
            return
            
                
                
        
        
        
        
        create(s,"")
        return res