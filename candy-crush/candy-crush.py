class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        stable=True
        rows,cols=len(board), len(board[0])
        crush=set()
        #find positions to be crushed
        #horizontal and vertical
        for i in range(rows):
            for j in range(cols):
                if j>=2 and board[i][j] and board[i][j-2]==board[i][j-1]==board[i][j]:
                    stable=False
                    crush.add((i,j-2))
                    crush.add((i,j-1))
                    crush.add((i,j))
                if i>=2 and board[i][j] and board[i-2][j]==board[i-1][j]==board[i][j]:
                    stable=False
                    crush.add((i-2,j))
                    crush.add((i-1,j))
                    crush.add((i,j))
        
        #crushdrop
        if not stable:
            for i,j in crush : board[i][j]=0
                
           
            for j in range(cols):
                startZero=rows-1
                for i in range(rows-1,-1,-1):
                    if board[i][j]==0 and startZero==rows:
                        startZero=i
                    if board[i][j]!=0 and startZero!=rows:
                        board[startZero][j], board[i][j]=board[i][j],board[startZero][j]
                        startZero-=1
        
        return board if stable else self.candyCrush(board)
                    
                        
            
        
        
        