class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        fixRows=set()
        fixCols=set()
        
        rows,cols=len(matrix),len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    fixRows.add(i)
                    fixCols.add(j)
        
        for row in fixRows:
            matrix[row]=[0]*cols
        
        #print(matrix)
        
        for col in fixCols:
            for row in range(rows):
                
                matrix[row][col]=0
                