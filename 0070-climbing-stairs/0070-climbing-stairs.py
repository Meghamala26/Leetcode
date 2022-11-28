class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo={0:0,1:1,2:2}
        
        def climbSteps(n):
            if n in memo:
                return memo[n]
            
            memo[n]=climbSteps(n-1)+climbSteps(n-2)
            return memo[n]
        
        climbSteps(n)
        return memo[n]
        