class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals=sorted(intervals, key=lambda x:x[0])
        #print(intervals)
        rooms=[]
        heapq.heappush(rooms, intervals[0][1])
        for x in intervals[1:]:
            start=x[0]
            end=x[1]
           
            if rooms[0]<=start:
                heapq.heappop(rooms)
                
            heapq.heappush(rooms, end)
                
                

                    
            
                
        return len(rooms)
                    
                
            
            
        
        
        