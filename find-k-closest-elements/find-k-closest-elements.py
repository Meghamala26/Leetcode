class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        closest=bisect_left(arr,x) # returns index of closest element
        print(closest)
        
        start,end=closest-1,closest
        
        
        while(end-start-1<k):
            if start>=0 and end<len(arr):
                if abs(arr[start]-x)<=abs(arr[end]-x):
                    start-=1
                else:
                    end+=1
            elif start<0:
                end+=1
            else:
                start-=1
        
        return arr[start+1:end]
            
            
        
        
        
        
        