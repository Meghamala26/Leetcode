class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum=float('-inf')
        i=0
        cumSum=0
        while(i<len(nums)):
            if cumSum+nums[i]>nums[i]:
                cumSum=cumSum+nums[i]
            else:
                cumSum=nums[i] 
            maxSum=max(maxSum, cumSum)
            i+=1
            
        return maxSum
            
            