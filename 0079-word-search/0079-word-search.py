class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows,cols=len(board), len(board[0])
        path=set()
        
        
        def search(i,j,index):
            if index==len(word):
                return True
            if i<0 or j<0 or i>=rows or j>=cols or (i,j) in path or board[i][j]!=word[index]:
                return False
            
            path.add((i,j))
            
            for rowoffset,coloffset in [(0,1),(0,-1),(1,0),(-1,0)]:
                if search(i+rowoffset,j+coloffset,index+1):
                    return True
            
            path.remove((i,j))
            return False
        
        
        for row in range(rows):
            for col in range(cols):
                if search(row,col,0):
                    return True
        return False
            