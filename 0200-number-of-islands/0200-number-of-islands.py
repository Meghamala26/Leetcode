class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count=0
        rows=len(grid)
        cols=len(grid[0])
        
        def dfs(row,col):
            if row>=0 and row<rows and col>=0 and col<cols and grid[row][col]=='1':
                grid[row][col]='0'
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)
            return
        
        for i in range(rows):
            for j in range(cols):
                #print(grid[i][j]=='1')
                if grid[i][j]=='1':
                    dfs(i,j)
                    count+=1
                    
        return count