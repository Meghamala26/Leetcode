# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        
        sentinel=ListNode(0)
        res=sentinel
        
        def reverse(head):
            cur=head
            while cur.next!=None:
                 cur=cur.next
            last=cur
            while last!=head:
                temp=last.next
                last.next=head
                head=head.next
                last.next.next=temp
                
            return head
        
        l1=reverse(l1)
        l2=reverse(l2)
        ##print(l2)
        carry=0
        while(l1!=None and l2!=None):
            new=ListNode(0)
            if l1.val+l2.val+carry>9:
                new.val=(l1.val+l2.val+carry)-10
                carry=1
            else:
                new.val=l1.val+l2.val+carry
                carry=0
            res.next=new
            res=res.next
            l1=l1.next
            l2=l2.next
           
        
        while(l1!=None):
            #print("1")
            new=ListNode(0)
            if l1.val+carry>9:
                new.val=(l1.val+carry)-10
                carry=1
            else:
                new.val=l1.val+carry
                carry=0
                
            res.next=new
            res=res.next
            l1=l1.next
            
        #print(res) 
        
        while(l2!=None):
            #print("2")
            new=ListNode(0)
            if l2.val+carry>9:
                new.val=(l2.val+carry)-10
                carry=1
            else:
                new.val=l2.val+carry
                carry=0   
            res.next=new
            res=res.next
            l2=l2.next
        
        #print(res)
        
        if carry==1:
            new=ListNode(1)
            res.next=new
            res=res.next
            
        #print(res)
        
        return reverse(sentinel.next)
                
        