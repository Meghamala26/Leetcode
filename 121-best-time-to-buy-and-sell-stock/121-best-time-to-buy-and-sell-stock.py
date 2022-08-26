class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minP=float('inf')
        maxProfit= float('-inf')
        
        for i,x in enumerate(prices):
            if x<=minP:
                minP=x
            
            if x-minP>=maxProfit:
                maxProfit=x - minP
                
        return maxProfit