class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map= {nums[i]:i for i in range(len(nums))}
        
        for i,x in enumerate(nums):
            if target-x in nums_map and nums_map[target-x]!=i:
                return [i,nums_map[target-x]]
        