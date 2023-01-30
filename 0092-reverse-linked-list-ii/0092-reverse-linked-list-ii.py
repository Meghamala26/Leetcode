# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        
        sentinel=ListNode(0)
        sentinel.next=head
        
        def reverse(beforeLeftNode,rightNode):
            leftNode=beforeLeftNode.next
            while(leftNode!=rightNode):
                rightNext=rightNode.next
                rightNode.next=leftNode
                leftNext=leftNode.next
                leftNode.next=rightNext
                leftNode=leftNext
            
            beforeLeftNode.next=rightNode
        
        
        cur=0
        beforeLeftNode=sentinel
        while(cur!=left-1):
            beforeLeftNode=beforeLeftNode.next
            cur+=1
        
        rightNode=beforeLeftNode
        while(cur!=right):
            rightNode=rightNode.next
            cur+=1
        
        reverse(beforeLeftNode,rightNode)
        return sentinel.next
            
            
                
                
        