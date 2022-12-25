# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        retHead=ListNode(0)
        ptr1,ptr2,retPtr=list1,list2,retHead
        
        while(ptr1!=None and ptr2!=None):
            if ptr1.val<=ptr2.val:
                retPtr.next=ptr1
                ptr1=ptr1.next
                
            else:
                retPtr.next=ptr2
                ptr2=ptr2.next
            retPtr.next.next=None
            retPtr=retPtr.next
            
        if ptr1!=None:
            retPtr.next=ptr1
        if ptr2!=None:
            retPtr.next=ptr2
            
        return retHead.next
        
            
            
                
            
        