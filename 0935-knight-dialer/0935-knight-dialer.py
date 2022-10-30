class Solution:
    def knightDialer(self, n: int) -> int:
        #in n-1 steps, we are going to end up on each of the digits.
        #dp[1..n-1][0..9] - rows representing steps and cols represent digits
        #dp[5][4]= dp[4,9]+dp[4,3]+dp[4,0] which stores the no of distinct phone nos that can be created if I reach 4 in 5 steps
        
        if n==1:
            return 10
    
        MOD=1e9 + 7
        dp=[[0 for x in range(10)] for y in range (n+2)]
        #print(dp)

        
        
        paths=[[4,6], [6,8], [7,9], [4,8], [0,3,9], [], [0,1,7], [2,6], [1,3], [2,4]]
        
        for j in range(0,10,1):
            dp[1][j]=1
        
        #print(dp)
            
        for i in range(2,n+1):
            for j in range(0,10,1):
                for x in paths[j]:
                    dp[i][j]+=dp[i-1][x]
                dp[i][j]=(dp[i][j]%MOD)
        #print(dp)
        res=0 
        for j in range(0,10):
            res+=dp[n][j]
            
        return int(res%MOD)
                
                        
        
        
        
        
        
        