class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        
        def choosePath(row,col):
            if row<0 or row>=m or col<0 or col>=n:
                return 0
            if row==m-1 and col==n-1:
                return 1
            if  str(row)+","+str(col) in memo:
                return memo[str(row)+","+str(col)]
            
            memo[str(row)+","+str(col)]=choosePath(row+1,col)+choosePath(row,col+1)
            return memo[str(row)+","+str(col)]
        
        return choosePath(0,0)
            
            
            
            
        