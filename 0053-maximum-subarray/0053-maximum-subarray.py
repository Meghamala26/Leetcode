class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start=end=0
        maxSum=curSum=nums[0]
        end=1
        while(end<len(nums)):
            while start<end and nums[end]>curSum+nums[end]:
                curSum-=nums[start]
                start+=1
            #print(start,end)
            curSum+=nums[end]
            maxSum=max(maxSum,curSum)    
            end+=1
        return maxSum
            