class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res=[]
        
        rows,cols=len(matrix), len(matrix[0])
        turns=(rows)//2
        k=0
        i,j=0,0
        flag1,flag2,flag3,flag4=0,0,0,1
        
        
        while(1):
            print(k)
            if k>0:
                j+=1
            while(flag4==1 and j<cols-k):
                res.append(matrix[i][j])
                j+=1
                flag1=1
            flag4=0
            j-=1
            i+=1
            while(flag1==1 and i<rows-k):
                res.append(matrix[i][j])
                i+=1
                flag2=1
            i-=1
            j-=1
            while(flag2==1 and j>=k):
                res.append(matrix[i][j])
                j-=1
                flag3=1
            
            k+=1
            if k>turns:
                break
            j+=1
            i-=1
            while(flag3 ==1 and i>=k):
                res.append(matrix[i][j])
                i-=1
                flag4=1
            i+=1
            flag1,flag2,flag3=0,0,0
            
        return res
            
        
        
        