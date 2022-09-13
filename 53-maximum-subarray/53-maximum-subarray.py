class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        left,right=0,0
        res=float('-inf')
        curSum=0
        while right < len(nums):
            curSum=max(curSum+nums[right], nums[right])
            res=max(res, curSum)
            right+=1
            
        return res
            
            