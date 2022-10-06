"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        
        def getNext(node):
            childNext=None
            while(node.next and not childNext):
                if node.next.left:
                    childNext=node.next.left
                elif node.next.right:
                    childNext=node.next.right
                else:
                    node=node.next
                    
            return childNext
                
            
        
        def setNext(node):
            if node:
                print (node.val)
            else:
                print ("None")
            if not node:
                return
            if node.left:
                if node.right:
                    node.left.next=node.right
                else:
                    node.left.next=getNext(node)
                
            if node.right:
                    node.right.next=getNext(node)
            
            
                    
            
            setNext(node.right)
            setNext(node.left)
                    
                    
                
            
            
        root.next=None
        setNext(root)
        return root
                
                
            
        