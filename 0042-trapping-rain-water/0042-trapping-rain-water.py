class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftMaxes=[0]*n
        rightMaxes=[0]*n
        
        for i in range(1,n):
            leftMaxes[i]=max(leftMaxes[i-1], height[i-1])
        
        for i in range(n-2,-1,-1):
            rightMaxes[i]=max(rightMaxes[i+1], height[i+1])
        
        count=0
        for i in range(n):
            water=min(leftMaxes[i],rightMaxes[i])-height[i]
            if water>0:
                count+=water
                
        return count
            
            
            
        
        
            
        
        