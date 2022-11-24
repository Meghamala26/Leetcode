class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def search(left,right,find):
            print(find)
            while(left<=right):
                mid=(left+right)//2
                if numbers[mid]==find:
                    return mid
                elif numbers[mid]<find:
                    left=mid+1
                else:
                    right=mid-1
            return -1
        
       
        if len(numbers)==2:
            return [1,2]
        
        for i in range(len(numbers)):
            
            val=search(i+1,len(numbers)-1,target-numbers[i])
            if val!=-1:
                return [i+1,val+1]
        
        
        