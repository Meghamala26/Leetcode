class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        nums_map=Counter(nums)
        
        for k,v in nums_map.items():
            if v>1:
                return True
            
        return False
            
        