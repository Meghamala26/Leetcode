class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        
        jobs=sorted(zip(difficulty,profit))
        maxProfit =bestMatch= j=0
        for skill in sorted(worker):
            while(j<len(jobs) and skill>=jobs[j][0]):
                bestMatch=max(bestMatch,jobs[j][1] )
                j+=1
            maxProfit+=bestMatch
                
        return maxProfit
                    
            
            
            
            
            
        