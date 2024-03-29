# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        cur=head

        while(cur.next!=None):
            cur=cur.next

        last=cur
        while(head!=last):
            lastNext=last.next
            last.next=head
            tmp=head.next
            head.next=lastNext
            head=tmp
        return head