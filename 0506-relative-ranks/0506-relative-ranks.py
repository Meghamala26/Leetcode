from queue import PriorityQueue
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        posMap={x:i for i,x in enumerate(score)}
        q=PriorityQueue()
        for i in range(n):
            q.put(-score[i])

        for i in range(n):
            val=-q.get(i)
            index= posMap[val]
            if i==0:
                score[index]="Gold Medal"
            elif i==1:
                score[index]="Silver Medal"
            elif i==2:
                score[index]="Bronze Medal"
            else:
                score[index]=str(i+1)
                
        return score
            
        
        
        
        
        
        