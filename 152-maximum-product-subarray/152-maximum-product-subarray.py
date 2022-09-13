class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxProd=nums[0]
        minProd=nums[0]
        res=nums[0]
        
        for x in nums[1:]:
            
            print(maxProd)
            print(minProd)
            
            temp=max(x,minProd*x,maxProd*x)
            minProd=min(x, minProd*x, maxProd*x)
            maxProd=temp
            
            res=max(res,maxProd)
            
            
        return res