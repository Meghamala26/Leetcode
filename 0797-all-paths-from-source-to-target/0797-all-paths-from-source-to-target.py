class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        paths=[]
        target=len(graph)-1
        
        def getPaths(node, curPath, target):
            
            curPath+=',' + str(node)
            if node==target:
                paths.append(curPath.split(','))
                return
            
            
            for x in graph[node]:

                getPaths(x, curPath, target)
                
                
            return
                
            
            
            
            
            
        
        
        for y in graph[0]:
            getPaths(y, "0", target)
            
        return paths
            