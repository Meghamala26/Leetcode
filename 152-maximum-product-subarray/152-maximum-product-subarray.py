class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProd=nums[0]
        minProd=nums[0]
        result=maxProd
        
        
        
        for i,x in enumerate(nums):
            if i==0:
                continue
            temp_max=max(x,maxProd*x,minProd*x)
            minProd=min(x,maxProd*x,minProd*x)
            
            maxProd=temp_max
            
            result=max(maxProd,result)
                
        return result
        
        
        