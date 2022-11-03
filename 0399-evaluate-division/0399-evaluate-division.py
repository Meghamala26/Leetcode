class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        chars=set()
        valMap=defaultdict(defaultdict)
        
        
        #building the graph
        for i in range(len(equations)):
            a,b=equations[i]
            val=values[i]
            chars.add(a)
            chars.add(b)
            valMap[a][b]= val
            valMap[b][a]= 1/val
        
        visited=set()
        def findPath(node,target,value):
            #print(node)
            #print(target)
            if target in valMap[node]:
                return (True,value*valMap[node][target])
            
            visited.add(node)
            for key in valMap[node].keys():
                if key not in visited:
                    found,res=findPath(key,target,value*valMap[node][key])
                    if found ==True:
                        return (found,res)
            
            visited.remove(node)
            return (False,-1)
            
            
            
                    
            
            
                
            
            
            
            
        
        #traversing the graph
        res=[]
        for i in range(len(queries)):
            A,B=queries[i]
            if A not in chars or B not in chars:
                res.append(-1.00000)
            elif A==B:
                res.append(1.00000)
            else:
                if B in valMap[A]:
                    res.append(valMap[A][B])
                else:
                    visited=set()
                    found,val=findPath(A,B,1)
                    res.append(val)
                    
        return res
                    
                    
            
            
            
        
        
        
        