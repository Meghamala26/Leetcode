class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start,end=0,len(nums)-1
        
        #678034
        if nums[start]<=nums[end]:
            return nums[start]
        
        while(start<=end):
            mid=start+(end-start)//2
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            
            if nums[mid]>nums[0]:
                start=mid
            else:
                end=mid-1
       
                
            
            
            
            
        
        