class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        
        def transpose():
            nonlocal matrix
            new=[[0 for i in range(n)] for j in range(n)]
            for r in range(n):
                for c in range(r+1,n):
                    matrix[c][r], matrix[r][c]=matrix[r][c], matrix[c][r]
                    
            
            
        
        def reflect():
            for r in range(n):
                left,right=0,n-1
                while(left<=right):
                    matrix[r][left],matrix[r][right]=matrix[r][right],matrix[r][left]
                    left+=1
                    right-=1
            
            
        
        transpose()
        print(matrix)
        reflect()
        