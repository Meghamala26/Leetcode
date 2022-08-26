class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        out_arr=[1]*len(nums)
        pref=1
        suff=1
        for i in range(1,len(nums)):
            pref=pref*nums[i-1]
            out_arr[i]=pref
            
        print(out_arr)
            
        for j in range(len(nums)-2,-1,-1):
            suff=suff*nums[j+1]
            out_arr[j]=out_arr[j]*suff
            
        print(out_arr)
        
        return out_arr
            
            
            
            
            