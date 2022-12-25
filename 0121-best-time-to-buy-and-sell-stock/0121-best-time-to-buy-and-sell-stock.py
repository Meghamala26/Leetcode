class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP=0
        minCost=prices[0]
        
        for i in range(1,len(prices)):
            minCost=min(minCost,prices[i])
            maxP=max(maxP,prices[i]-minCost)
        return maxP
            
        