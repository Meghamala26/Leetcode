class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n=len(nums2)
        cpynums1=nums1[:len(nums1)-n]
        
        i,j,k=0,0,0
        
        while(i<len(cpynums1) and j<n):
            if cpynums1[i]<=nums2[j]:
                nums1[k]=cpynums1[i]
                i+=1
            else:
                nums1[k]=nums2[j]
                j+=1
            
            k+=1
        while(i<len(cpynums1)):
            nums1[k]=cpynums1[i]
            i+=1
            k+=1
        while(j<n):
            nums1[k]=nums2[j]
            j+=1
            k+=1
        
        
        