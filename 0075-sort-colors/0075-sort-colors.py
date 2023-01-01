class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        start,end=0,len(nums)-1
        curr=0
        
        while(curr<=end):
            if nums[curr]==2:
                nums[curr],nums[end]=nums[end],nums[curr]
                end-=1
            elif nums[curr]==0:
                nums[curr],nums[start]=nums[start],nums[curr]
                start+=1
                curr+=1
            else:
                curr+=1
                