class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo={}
        def getMaxLoot(index):
            
            if index>=len(nums):
                return 0
            
            if index in memo:
                return memo[index]
            
            profit=max(nums[index]+getMaxLoot(index+2), getMaxLoot(index+1))
            memo[index]=profit
            return profit
        
        return getMaxLoot(0)
            
        
        