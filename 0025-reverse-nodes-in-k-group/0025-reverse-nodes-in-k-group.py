# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        sentinel=ListNode(0)
        sentinel.next=head
        beforeStart=endNode=sentinel

        def reverse_list(beforeStart,endNode):

            start=beforeStart.next
            remStart=start
            while(start!=endNode):
                endNxt=endNode.next
                endNode.next=start
                startNxt=start.next
                start.next=endNxt
                start=startNxt
            beforeStart.next=endNode
            return remStart


        def traverse_k_steps(beforeStart,endNode):
            beforeStart=endNode
            count=1
            while(count<=k and endNode!=None):
                endNode=endNode.next
                count+=1
            return beforeStart,endNode

        beforeStart,endNode=traverse_k_steps(beforeStart,endNode)
        while(endNode!=None):
            remStart=endNode=reverse_list(beforeStart,endNode)
            beforeStart,endNode=traverse_k_steps(beforeStart,endNode)
        
        return sentinel.next







