from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp=[-x for x in nums]
        heapq.heapify(temp)
        for i in range(k-1):
            heapq.heappop(temp)
        return -temp[0]
        
        
        