class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        def compressMatrix(mat):
            matDict=collections.defaultdict(list)
            rows,cols=len(mat), len(mat[0])
            
            for i in range(rows):
                for j in range(cols):
                    if mat[i][j]!=0:
                        matDict[i].append((mat[i][j],j))
                        
            
            return matDict
        
        matDict1=compressMatrix(mat1)
        matDict2=compressMatrix(mat2)
        m,k,n=len(mat1), len(mat1[0]),len(mat2[0])
        
        
        res=[[0 for i in range(n)] for j in range(m)]
        
        for row1,colList in matDict1.items():
            for (val1,col1) in colList:
                for val2,col2 in matDict2[col1]:
                    res[row1][col2]+=val1*val2
        
        return res
               
            
            
        