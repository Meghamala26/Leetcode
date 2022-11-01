class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        
        res=[[1],[1,1]]
        i=3
        while(i<=numRows):
            level=[]
            level.append(1)
            for j in range(0,len(res[i-2])-1):
                level.append(res[i-2][j]+res[i-2][j+1])         
            level.append(1)
            res.append(level)
            i+=1
        
        return res