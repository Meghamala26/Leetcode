class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idxMap={}
        for i in range(len(nums)):
            if (target-nums[i]) in idxMap:
                return [i,idxMap[(target-nums[i])]]
            else:
                idxMap[nums[i]]=i
        
        