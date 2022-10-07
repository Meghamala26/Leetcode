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
                    lastchild=lastchild.next
                    if lastchild.child and not nextCurr:
                        nextCurr=lastchild
                curr.next=curr.child
                curr.child.prev=curr
                lastchild.next=temp
                if temp:
                    temp.prev=lastchild
                curr.child=None
                if nextCurr:
                    curr=nextCurr
                else:    
                    curr=curr.next
            else:
                curr=curr.next
                    
        return head
                    
                    
                
                
        