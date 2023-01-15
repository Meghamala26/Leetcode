class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen=float('inf')
        start,end=0,0
        curSum=0
        while(end<len(nums)):
            curSum+=nums[end]
            if curSum>=target:
                while(curSum>=target):
                    minLen=min(minLen,end-start+1)
                    curSum-=nums[start]
                    start+=1  
            end+=1 
        return minLen if minLen!=float('inf') else 0