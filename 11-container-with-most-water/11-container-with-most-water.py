class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        
        maxArea=0
        left=0
        right=len(height)-1
        
        while(left<=right):
            if height[left]<=height[right]:
                maxArea=max(height[left]*(right-left), maxArea)
                left+=1
            else:
                maxArea=max(height[right]*(right-left), maxArea)
                right-=1
                    
        return maxArea
                
            
                
            
        
        