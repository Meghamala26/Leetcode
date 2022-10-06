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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        root.next=None
        
        def getNext(node):
            
            if not node:
                return
            if node.left:
                node.left.next=node.right
                getNext(node.left)
            if node.right:
                if node.next:
                    node.right.next=node.next.left
                else:
                    node.right.next=None
                    
            
                getNext(node.right)
            
        
        getNext(root)
        return root
        