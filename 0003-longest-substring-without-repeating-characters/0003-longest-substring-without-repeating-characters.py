class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)==0:
            return 0
        
        curMap={} # char in cur String: index
        start=0
        maxLen=float('-inf')
        end=0
        
        while(end<len(s)):
            if s[end] not in curMap:
                curMap[s[end]]=end
            else:
                maxLen=max(maxLen, end-start)
                #remove all chars from curMap between cur start and repeated char
                for i in range(start,curMap[s[end]]):
                    del curMap[s[i]]
                start=curMap[s[end]]+1
                curMap[s[end]]=end
            end+=1
        
        return max(maxLen, end-start)