class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        heapq.heapify(heap)
        
        n=len(matrix)
            
        for i in range(n):
            for j in range(n):
                if len(heap)<k:
                    
                    heapq.heappush(heap,-matrix[i][j])
                    
                else:
                    if matrix[i][j]<-heap[0]:
                        
                        heapq.heappop(heap)
                        print(-matrix[i][j])
                        
                        heapq.heappush(heap,-matrix[i][j])
                    else:
                        continue
        return -heap[0]