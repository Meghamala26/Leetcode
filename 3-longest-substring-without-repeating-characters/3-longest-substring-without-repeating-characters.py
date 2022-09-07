class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)<=1:
            return len(s)
        
        
        index_map={}
        
        left=right=0
        maxLen=float('-inf')
        
        for right,x in enumerate(s):
            if x not in index_map:
                index_map[x]=right
            else:
                left = max(left, index_map[x]+1)
                index_map[x]=right
                
            maxLen=max(maxLen, right-left+1)
    
        return maxLen
                    
                
                