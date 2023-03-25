import bisect
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if intervals==[]:
            return [newInterval]
        
        
        pos=bisect.bisect_left(intervals, newInterval)
        print(pos)
        
        newIntervals=intervals[:pos]
        if pos==0:
            newIntervals.append(newInterval)
        if pos ==len(intervals):
            if newInterval[0]<=newIntervals[-1][1]:
                newIntervals[-1][1]=max(newInterval[1],newIntervals[-1][1])
            else:
                newIntervals.append(newInterval)
        
        
        i=pos
        
        
        while(i<len(intervals)):
            if i==pos:
                if newInterval[0]<=newIntervals[-1][1]:
                    newIntervals[-1][1]=max(newInterval[1],newIntervals[-1][1])
                else:
                    newIntervals.append(newInterval)
                
            if intervals[i][0] <= newIntervals[-1][1] :
                newIntervals[-1][1]=max(intervals[i][1],newIntervals[-1][1])
            else:
                newIntervals.append(intervals[i])
                
            i+=1
            
        return newIntervals
            
        
        
            
            
            
        
        
        
        