class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        sortedMatrix=[]
        heapq.heapify(sortedMatrix)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if len(sortedMatrix)<k:
                    heapq.heappush(sortedMatrix, -matrix[i][j])
                else:
                    if -sortedMatrix[0]>matrix[i][j]:
                        heapq.heappop(sortedMatrix)
                        heapq.heappush(sortedMatrix, -matrix[i][j])
                        
        return -sortedMatrix[0]
        