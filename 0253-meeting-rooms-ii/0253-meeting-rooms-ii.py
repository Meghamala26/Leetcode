class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        
        intervals=sorted(intervals, key=lambda x:x[0])
        print(intervals)
        rooms=[intervals[0]]
        for x in intervals[1:]:
            start=x[0]
            end=x[1]
            flag=0
            #print(x)
            #print(rooms)
            for y in rooms:
                rstart=y[0]
                rend=y[1]
                if (start<=rstart and end<=rstart) or (start>=rend and end>=rend):
                    #print(1)
                    y[0]=min(start,rstart)
                    y[1]=max(end,rend)
                    flag=1
                    break
                    
            if flag==0: 
                #print(0)
                rooms.append([start,end])
                
        return len(rooms)
                    
                
            
            
        
        
        