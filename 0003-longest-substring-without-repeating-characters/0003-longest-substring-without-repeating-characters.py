class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
       
        start,end=0,0
        curSet=set()
        maxLen=float('-inf')
        while(end<len(s)):
            
            if s[end] not in curSet:
                curSet.add(s[end])
            else:
                #print(s[start:end])
                while(curSet and s[end] in curSet):
                    #print(start)
                    curSet.remove(s[start])
                    start+=1
                curSet.add(s[end])
            maxLen=max(maxLen,end-start+1)
            end+=1
                
        return maxLen if maxLen!=float('-inf') else 0
                
                    
                
            
            
        