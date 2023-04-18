class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numsMap={}
        for i in range(len(nums)):
            print(nums[i])
            if nums[i] in numsMap:
                print(1)
                return True
            else:
                numsMap[nums[i]]=i
        return False
        