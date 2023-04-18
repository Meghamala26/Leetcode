class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP=0
        minCost=prices[0]
        
        for i in range(1,len(prices)):
            maxP=max(maxP,prices[i]-minCost)
            minCost=min(minCost, prices[i])
        
        return maxP
            
        
        
        