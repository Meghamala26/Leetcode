class Solution:
    def setMarker(self,matrix, i, j, row, col):
            for x in range(col):
                if matrix[i][x]!=0:
                    matrix[i][x]='S'
            for x in range(row):
                if matrix[x][j]!=0:
                    matrix[x][j]='S'
                    

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col= len(matrix), len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    self.setMarker(matrix,i,j,row,col)
                    
        for i in range(row):
            for j in range(col):
                if matrix[i][j]=='S':
                    matrix[i][j]=0
                    
        
                
                
                
        