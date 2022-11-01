class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroIdx=-1
        
        i=0
        while(i<len(nums)):
            if nums[i]==0 and zeroIdx==-1:
                zeroIdx=i
            elif nums[i]!=0 and zeroIdx!=-1:
                nums[i],nums[zeroIdx]=nums[zeroIdx],nums[i]
                zeroIdx+=1
            i+=1
        
        
        
       
            