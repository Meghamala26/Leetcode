class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        n=len(difficulty)
        m=len(worker)
        jobs=[]
        for i in range(n):
            jobs.append((difficulty[i],profit[i]))
        
        jobs.sort()
        
        maxProfitSoFar=[0]*n
        maxProfitSoFar[0]=jobs[0][1]
        
        for i in range(1,n):
            maxProfitSoFar[i]=max(maxProfitSoFar[i-1],jobs[i][1])
        
        maxProfit=0
        for skill in worker:
            
            bestIndex=-1
            start=0
            end=n-1
            
            while(start<=end):
                mid=start+(end-start)//2
                
                if jobs[mid][0]<=skill:
                    bestIndex=mid
                    start=mid+1
                else:
                    end=mid-1
            
            if bestIndex!=-1:
                maxProfit+=maxProfitSoFar[bestIndex]
        
        return maxProfit
                
            
            
            
            
            
        