class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols=len(board),len(board[0])
        
        def checkWord(row,col,index,visited):
            #print(index, visited)
            if row<0 or row>=rows or col<0 or col>=cols or (row,col) in visited or board[row][col]!=word[index]:
                return False
            
            if index==len(word)-1:
                return True
            
            visited.add((row,col))
            
            
            ret=checkWord(row+1,col,index+1,visited) or checkWord(row-1,col,index+1,visited) or checkWord(row,col+1,index+1,visited) or checkWord(row,col-1,index+1,visited)
            
            visited.remove((row,col))
            return ret
        
            
        
        
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]==word[0]:
                    if checkWord(i,j,0,set()):
                        return True
        return False
        