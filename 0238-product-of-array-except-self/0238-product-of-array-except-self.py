class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N=len(nums)
        suffix=[1]*N
        
        for i in range(N-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        
        print(suffix)
        
        prefix=[1]*N
        
        for i in range(1,len(nums),1):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        output=[suffix[i]*prefix[i] for i in range(N)]
        return output
        