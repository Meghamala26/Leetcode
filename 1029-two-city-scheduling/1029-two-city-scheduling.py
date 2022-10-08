class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n=len(costs)
        limit=n//2
        costs.sort(key = lambda x: x[0]-x[1])
        
        cost=0
        for i in range(limit):
            cost+=costs[i][0]+costs[i+limit][1]
        return cost
        
        
        
       
        
        