# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next==None:
            return False
        cur=head
        while(cur.next!=None):
            if cur.val!='Found':
                cur.val='Found'
                
            else:
                return True
            cur=cur.next
            
        return False
            