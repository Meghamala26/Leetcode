class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        start=0
        visited={}
        maxLen=float('-inf')
        curLen=0
        n=len(s)
        if n<=1:
            return n
        
        for i,x in enumerate(s):
            
            if x not in visited:
                visited[x]=i
                
            else:
                temp=visited[x]+1
                
                for j in range(start, temp):
                    del visited[s[j]]
                start=temp
                visited[x]=i
               
            maxLen=max(maxLen,i-start+1)
            
        return maxLen
            
            
        
        