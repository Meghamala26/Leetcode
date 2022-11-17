# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start,end=1,n
        firstBad=-1
        while(start<=end):
            mid=(start+end)//2
            check=isBadVersion(mid)
            if check:
                firstBad=mid
                end=mid-1
            else:
                start=mid+1
        return firstBad
                
                
        