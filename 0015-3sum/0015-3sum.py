class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output=set()
        for i in range(len(nums)-2):
            low,high=i+1,len(nums)-1
            while(low<high):
                curSum=nums[i]+nums[low]+nums[high]
                if curSum==0:
                    output.add((nums[i],nums[low],nums[high]))    
                if curSum<0:
                    low+=1
                else:
                    high-=1
        return list(output)