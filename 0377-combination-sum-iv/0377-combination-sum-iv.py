class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        memo={}
        def getComb(remTarget):
            if remTarget<0:
                return 0
            if remTarget==0:
                return 1
            if remTarget in memo:
                return memo[remTarget]
            
            res=0
            for x in nums:
                res+=getComb(remTarget-x)
            
            memo[remTarget]=res
            return res
                
            
            
        
        getComb(target)
        return memo[target]
            
        