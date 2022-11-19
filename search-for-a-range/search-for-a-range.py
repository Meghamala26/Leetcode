class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def searchTarget(left,right):
            while(left<=right):
                mid=(left+right)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return -1
        
        
        #left,right=0,len(nums)-1
        firstOccurence=searchTarget(0,len(nums)-1)
        start=end=firstOccurence
        if firstOccurence==-1:
            return [-1,-1]
        else:
            while(1):
                first=searchTarget(0,start-1)
                if first==-1:
                    break
                start=first
            while(1):
                last=searchTarget(end+1,len(nums)-1)
                if last==-1:
                    break
                end=last
            return [start,end]
            
        
            
            
        