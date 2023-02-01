# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        

        if not head:
            return head
        sentinel=ListNode(0)
        sentinel.next=head
        count=0
        cur=sentinel
        kNode=None
        while(cur.next!=None):
            cur=cur.next
            count+=1
            if count==k:
                kNode=cur

        length=count
        findCount=length-k+1
        count=0
        cur=sentinel
        while(cur.next!=None):
            cur=cur.next
            count+=1
            if count==findCount:
                cur.val,kNode.val=kNode.val,cur.val




        return head

        