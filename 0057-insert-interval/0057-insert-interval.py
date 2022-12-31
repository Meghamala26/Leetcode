class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals)==0:
            return [newInterval]
        
        output=[]
        idx = bisect.bisect_left(intervals,newInterval)
        
        output=intervals[:idx]
        
        for i in range(idx-1,len(intervals)):
            #lastStart,lastEnd=output[-1][0],output[-1][1]
            
            if i==idx-1:
                #handle newInterval
                if output and output[-1][0]<=newInterval[0]<=output[-1][1] :
                    output[-1][1]=max(output[-1][1],newInterval[1])
                else:
                    output.append(newInterval)
                    
            else:
                #handle existing Intervals
                if output and output[-1][0]<=intervals[i][0]<=output[-1][1]:
                    output[-1][1]=max(output[-1][1],intervals[i][1])
                else:
                    output.append(intervals[i])
                    
        return output
                
                
            
            
            
                
            
            
        
        
        