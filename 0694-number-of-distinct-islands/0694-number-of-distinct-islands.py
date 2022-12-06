class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        numRows,numCols=len(grid),len(grid[0])
        def getIsland(row,col):
            if row<0 or row>=numRows or col<0 or col>=numCols or grid[row][col]==0 or (row,col) in seen :
                return
            
            seen.add((row,col))
            current_island.add((row-row_origin, col-col_origin))
            getIsland(row+1,col)
            getIsland(row-1,col)
            getIsland(row,col-1)
            getIsland(row,col+1)
            
        
        seen=set()
        unique_islands=set()
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current_island=set()
                row_origin=row
                col_origin=col
                getIsland(row,col)
                
                if current_island:
                    unique_islands.add(frozenset(current_island))
        return len(unique_islands)
            
            
            
            
            