class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        minHeap=[]
        intervals.sort(key=lambda x:x[0])
        heapq.heappush(minHeap,intervals[0][1])

        for i in range(1,len(intervals)):
            if minHeap[0]<=intervals[i][0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap,intervals[i][1])
            

        return len(minHeap)