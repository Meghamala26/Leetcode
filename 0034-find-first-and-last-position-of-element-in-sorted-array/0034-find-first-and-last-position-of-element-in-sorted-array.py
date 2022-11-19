class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def search(isFirst):
            left,right=0,len(nums)-1
            while(left<=right):
                mid=(left+right)//2
                if nums[mid]==target:
                    if isFirst==True:
                        if mid==0 or nums[mid-1]!=target:
                            return mid
                        else:
                            right=mid-1
                    else:
                        if  mid==len(nums)-1 or nums[mid+1]!=target :
                            return mid
                        else:
                            left=mid+1
                elif nums[mid]<target:
                    left=mid+1
                else:
                    right=mid-1
            return -1
        
        startIndex=search(True)
        if startIndex==-1:
            return [-1,-1]
        endIndex=search(False)
        return [startIndex,endIndex]
        