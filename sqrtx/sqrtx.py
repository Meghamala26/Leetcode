class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        left,right=1,x
        sqrt=-1
        
        while(left<=right):
            mid=(left+right)//2
            if mid**2<=x:
                sqrt=mid
                left=mid+1
            else:
                right=mid-1
        return sqrt
        
        