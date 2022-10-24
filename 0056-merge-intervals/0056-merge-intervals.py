class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by start time
        intervals.sort(key = lambda x:x[0])
        res=[intervals[0]]
        
        for time in intervals[1:]:
            if time[0]<=res[-1][1]:
                start=res[-1][0]
                end=res[-1][1]
                res.pop()
                res.append([start, max(end,time[1])])
            else:
                res.append(time)
                
        return res
        
        
        