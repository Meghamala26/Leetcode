class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count=Counter(t)
        wind_count={}
        required=len(t_count)
        found=0
        start,end=0,0
        ans=(float('inf'),start,end)
        while(end<len(s)):
            curChar=s[end]
            wind_count[curChar]=wind_count.get(curChar,0)+1
            
            if curChar in t_count and t_count[curChar]==wind_count[curChar]:
                found+=1
                
            while(start<=end and found==required):
                
                ch=s[start]
                if end-start+1<ans[0]:
                    ans=(end-start+1,start,end)
                wind_count[ch]-=1
                if ch in t_count and wind_count[ch]<t_count[ch]:
                    found-=1    
                start+=1

            end+=1
        
        return "" if ans[0]==float('inf') else s[ans[1]:ans[2]+1]
                
        
        