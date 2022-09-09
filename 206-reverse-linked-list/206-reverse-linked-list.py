# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if head==None:
            return None
        prev=ListNode(0)
        prev.next=head
        
        tail=head
        
        while(tail.next!=None):
            tail=tail.next
        
        while(tail!=head):
            prev.next=head.next
            head.next=tail.next
            tail.next=head
            head=prev.next
            
            
                
        return prev.next
        
            
            
        
            
            
        