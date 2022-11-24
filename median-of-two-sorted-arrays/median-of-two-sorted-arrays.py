class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j=0,0
        nums=[]
        
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<=nums2[j]):
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
        while(i<len(nums1)):
            nums.append(nums1[i])
            i+=1   
        while(j<len(nums2)):
            nums.append(nums2[j])
            j+=1 
        
        print(nums)
        if len(nums)%2==0:
            mid=len(nums)//2
            return (nums[mid]+nums[mid-1])/2
        else:
            return nums[(len(nums)//2)]
        
        
        