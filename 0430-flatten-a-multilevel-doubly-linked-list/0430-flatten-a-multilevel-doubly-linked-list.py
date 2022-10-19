"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        curr=head
        while(curr):
            if curr.child:
                temp=curr.next
                lastchild=curr.child
                nextCurr=None
                while lastchild.next:
                    
                    if lastchild.child and not nextCurr:
                        nextCurr=lastchild
                    lastchild=lastchild.next
                curr.next=curr.child
                curr.child.prev=curr
                lastchild.next=temp
                if temp:
                    temp.prev=lastchild
                curr.child=None
                if nextCurr:
                    curr=nextCurr
                else:    
                    curr=lastchild
            else:
                curr=curr.next
                    
        return head
                    
                    
                
                
        