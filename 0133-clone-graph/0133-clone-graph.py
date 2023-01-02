"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        nodeMap={}
        def cloneNode(old,new):
            if old.neighbors:
                new.neighbors=[]
            
                for n in old.neighbors:
                    if n.val not in nodeMap:
                        newNode=Node(n.val)
                        nodeMap[n.val]=newNode
                        new.neighbors.append(newNode)
                        cloneNode(n,newNode)
                    else:
                        new.neighbors.append(nodeMap[n.val])
        
        if not node:
            return None
        
        newNode=Node(node.val)
        nodeMap[node.val]=newNode
        cloneNode(node,newNode)
        return newNode
                    
                
            
            
            
        
        