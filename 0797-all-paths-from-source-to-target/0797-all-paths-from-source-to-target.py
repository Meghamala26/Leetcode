class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths=[]
        target=len(graph)-1
        
        def getPaths(node, curPath):
            if node==target:
                paths.append(list(curPath))
                return
            for x in graph[node]:
                curPath.append(x)
                getPaths(x, curPath)
                curPath.pop()  
            return

        getPaths(0, [0])   
        return paths
            