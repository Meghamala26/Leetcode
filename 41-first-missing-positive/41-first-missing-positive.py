class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        nums= set(nums)
        for i in range(1,max(nums)+1):
            if i in nums:
                continue
            else:
                return i
        if 1 not in nums:
            return 1
        else:
            return max(nums)+1
            
        
                
                
            
        