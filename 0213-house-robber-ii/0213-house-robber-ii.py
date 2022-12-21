class Solution:
    def rob(self, nums: List[int]) -> int:
        memo1={}
        memo2={}
       
        def robMax(ind,visited):
            if ind==len(nums)-1 and 0 in visited:
                #print("Found circle")
                memo1[ind]=0
                return 0
            if ind>=len(nums):
                return 0
            if ind in memo1:
                return memo1[ind]
            cpy=visited.copy()
            cpy.add(ind)
            maxLoot=max(nums[ind]+robMax(ind+2,cpy), robMax(ind+1,visited))
            memo1[ind]=maxLoot
            return maxLoot
        
        def robMaxRev(ind,visited):
            if ind==0 and len(nums)-1 in visited:
                #print("Found circle")
                memo2[ind]=0
                return 0
            if ind<0:
                return 0
            if ind in memo2:
                return memo2[ind]
            cpy=visited.copy()
            cpy.add(ind)
            maxLoot=max(nums[ind]+robMaxRev(ind-2,cpy), robMaxRev(ind-1,visited))
            memo2[ind]=maxLoot
            return maxLoot
        
        
        
        robMax(0,set())
        robMaxRev(len(nums)-1,set())
       
        return max(memo1[0],memo2[len(nums)-1])
            
        