# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head.next==None:
            return head
        def findMid(head):
            slow, fast=head, head
            while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
            return slow


        def reverse(mid):
            sentinel=ListNode(0)
            sentinel.next=mid
            while(mid.next!=None):
                attachNode=mid.next
                attachNext=attachNode.next
                mid.next=attachNext
                attachNode.next=sentinel.next
                sentinel.next=attachNode
            return sentinel

        mid=findMid(head)
        cur=head
        #setting node previous to mid to None
        while(cur.next!=mid):
            cur=cur.next
        cur.next=None
        sentinel = reverse(mid)
        #reorder list
        midNode=sentinel.next
        attachToNode=head
        while(attachToNode!=None):
            nextMid=midNode.next
            nextAttach=attachToNode.next
            attachToNode.next=midNode
            midNode.next=nextAttach
            if nextMid!=None and nextAttach==None:
                attachToNode=midNode
            else:
                attachToNode=nextAttach
            midNode=nextMid
        