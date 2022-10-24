class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by start time
        intervals.sort(key = lambda x:x[0]) #nlogn
        res=[intervals[0]]
        
        for time in intervals[1:]: #n-1
            if time[0]<=res[-1][1]:
                res[-1][1]=max(res[-1][1],time[1])
            else:
                res.append(time)
                
        return res
        
        
        