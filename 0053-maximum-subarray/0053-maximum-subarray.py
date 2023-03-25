class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        end=1
        curSum=nums[0]
        maxSum=nums[0]
        while(end<len(nums)):
            if curSum+nums[end]>nums[end]:
                curSum+=nums[end]
            else:
                curSum=nums[end]
            maxSum=max(maxSum, curSum)
            end+=1
        
        return maxSum
            
            
        
        