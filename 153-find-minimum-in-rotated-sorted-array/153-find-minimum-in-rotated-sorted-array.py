class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        curMin=nums[0]
        
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                continue
            else:
                curMin=min(curMin,nums[i])
                
        return curMin
            
        