class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rotten=[]
        fresh=0
       
        
        ROWS,COLS=len(grid),len(grid[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2 :
                    rotten.append((i,j))
                else:
                    continue
        
        
        if fresh==0:
            return 0
        
        # from each rotten orange, traverse BFS to reach a fresh orange. If cant reach any new fresh orange, return False. Else return True.
        def rot():
            nonlocal fresh
            rotten.append((-1,-1))
            directions=[(-1,0),(1,0),(0,-1),(0,1)]
            while rotten:
                row,col=rotten.pop(0)
                if row==-1 and col==-1:
                    if len(rotten)!=0:
                        return True
                    else:
                        return False
                else:
                    for x,y in directions:
                        if row+x>=0 and row+x<ROWS and col+y>=0 and col+y<COLS and grid[row+x][col+y]==1:
                            fresh-=1
                            rotten.append((row+x,col+y))
                            grid[row+x][col+y]=2
        
        
        minutes=0
        while(1):
            if not rot():
                break
            minutes+=1
        
        if fresh==0:
            return minutes
        else:
            return -1
                    
                
                    
                
            