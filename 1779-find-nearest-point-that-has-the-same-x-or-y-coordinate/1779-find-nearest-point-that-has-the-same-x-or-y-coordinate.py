class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        
        minDis=float('inf')
        ret=[]
        
        for i,(x1,y1) in enumerate(points):
            if x1==x or y1==y:
                if minDis>(abs(x1-x)+abs(y1-y)):
                    minDis=(abs(x1-x)+abs(y1-y))
                    ret=[i]
                elif minDis==(abs(x1-x)+abs(y1-y)):
                    ret.append(i)
                else:
                    continue
                    
        
        return min(ret) if len(ret)!=0 else -1
        