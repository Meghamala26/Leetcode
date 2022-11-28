class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo={0:0}
        
        def getMinCoins(amnt):
            if amnt<0:
                return -1
            if amnt in memo:
                return memo[amnt]
            
            minCost=float('inf')
            
            for x in coins:
                res=getMinCoins(amnt-x)
                if res!=-1:
                    minCost=min(minCost,res+1)
            
            memo[amnt]=minCost if minCost!=float('inf') else -1
            return memo[amnt]
                
        
        getMinCoins(amount)
        return memo[amount]
                
        