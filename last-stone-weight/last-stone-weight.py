class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        heapq.heapify(stones)
        
        while(len(stones)>1):
            first=-heapq.heappop(stones)
            second=-heapq.heappop(stones)
            #print(first)
            #print(second)
            if first!=second:
                heapq.heappush(stones, -abs(first-second))
        
        if len(stones)>=1:
            return -stones[0]
        else:
            return 0
                
                
            
        