class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left,right=0,len(letters)-1
        smallest=-1
        
        while(left<=right):
            mid=(left+right)//2
            if letters[mid]<=target:
                smallest=mid
                left=mid+1
            else:
                right=mid-1
        
        return letters[smallest+1] if smallest<len(letters)-1 else letters[0]