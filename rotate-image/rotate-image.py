class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)-1
        turns=len(matrix)//2
        i,j=0,0
        while(turns>0):
            for k in range(j,n-j):
                temp=matrix[n-k][i]
                matrix[n-k][i]=matrix[n-i][n-k]
                matrix[n-i][n-k]=matrix[k][n-i]
                matrix[k][n-i]=matrix[i][k]
                matrix[i][k]=temp
            turns-=1
            i+=1
            j+=1
            
                
            