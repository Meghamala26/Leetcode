class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s)<=1:
            return len(s)
        
        
        freq_map={}
        
        left=right=0
        maxLen=float('-inf')
        
        for right,x in enumerate(s):
            if x not in freq_map:
                freq_map[x]=1
            else:
                while(freq_map[x]==1):
                    freq_map[s[left]]-=1
                    left+=1
                freq_map[x]=1
                
            maxLen=max(maxLen, right-left+1)
    
        return maxLen
                    
                
                