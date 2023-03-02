import heapq
class MedianFinder:

    def __init__(self):
        self.maxSmall=[]
        self.minLarge=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxSmall,-num)
        heapq.heappush(self.minLarge,-heapq.heappop(self.maxSmall))
        
        if len(self.minLarge) > len(self.maxSmall):
            heapq.heappush(self.maxSmall,-heapq.heappop(self.minLarge) )
        
        

    def findMedian(self) -> float:
        ##print(self.minLarge)
    
        return (-self.maxSmall[0]+self.minLarge[0])/2 if len(self.maxSmall)==len(self.minLarge) else -self.maxSmall[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()