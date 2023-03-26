class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(mat), len(mat[0])
        
        queue=[]
        
        dist=[[float('inf') for c in range (COLS)] for r in range(ROWS)]
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c]==0:
                    dist[r][c]=0
                    queue.append((r,c))
        
        while(len(queue)>0):
            curR, curC=queue.pop(0)
            for (r,c) in [[-1,0],[1,0], [0,-1], [0,1]]:
                neighborR, neighborC=curR+r, curC+c
                if neighborR>=0 and neighborR<ROWS and neighborC>=0 and neighborC<COLS:
                    if dist[neighborR][neighborC]>dist[curR][curC]+1:
                        dist[neighborR][neighborC]=dist[curR][curC]+1
                        queue.append((neighborR, neighborC))
                        
        return dist
                
            