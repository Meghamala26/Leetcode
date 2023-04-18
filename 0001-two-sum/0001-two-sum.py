class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idxMap = {nums[i] : i for i in range(len(nums))}
        for i in range(len(nums)):
            if (target - nums[i]) in idxMap and idxMap[(target - nums[i])]!=i:
                return [i,idxMap[target - nums[i]]]
        
        