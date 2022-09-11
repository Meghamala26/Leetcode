class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        cur=1
        for i in range(len(nums)):
            if i==0:
                res.append(1)
            else:
                cur=cur*nums[i-1]
                res.append(cur)
                
        cur=1      
        for i in range(len(nums)-1,-1,-1): 
            
            if i==len(nums)-1:
                continue
            else:
                cur=cur*nums[i+1]
                res[i]=res[i]*cur
                
            
        return res