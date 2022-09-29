class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map={}
        
        for i,x in enumerate(nums):
            if (target-x) in nums_map:
                return [i, nums_map[target-x]]
            else:
                nums_map[x]=i
                
                
        
        
        