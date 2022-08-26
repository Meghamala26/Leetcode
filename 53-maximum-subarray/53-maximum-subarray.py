class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum=float('-inf')
        cur=0
        
        for x in nums:
            cur=max(cur+x,x)
            maxSum=max(maxSum, cur)
            
        return maxSum
        
        