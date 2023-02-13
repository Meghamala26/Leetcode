# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head

        def reverse(beforeStart, end):
            newEnd=beforeStart.next
            while beforeStart.next!=end:
                afterEnd=end.next
                nextStart=beforeStart.next.next
                end.next=beforeStart.next
                beforeStart.next.next=afterEnd
                beforeStart.next=nextStart

            return newEnd
        
        beforeStart=head
        l=2

        while (beforeStart.next!=None):
            cur=beforeStart.next
            count=1
            while(cur.next!=None and count<l):
                cur=cur.next
                count+=1    
            if count%2==0:
                newEnd=reverse(beforeStart, cur)
                beforeStart=newEnd
            else:
                beforeStart=cur
            l+=1

        return head
        