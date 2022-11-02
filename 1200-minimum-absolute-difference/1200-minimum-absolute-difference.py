class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        if len(arr)==2:
            if arr[0]<arr[1]:
                return [[arr[0], arr[1]]]
            else:
                return [[arr[1], arr[0]]]
        
        arr=sorted(arr)
        #print(arr)
        diffMap={}
        minDiff=float('inf')
        for i in range(len(arr)-1):
            diff=abs(arr[i]-arr[i+1])
            if minDiff>diff:
                minDiff=diff
                diffMap={}
                diffMap[minDiff]=[[arr[i], arr[i+1]]]
            elif minDiff==diff:
                diffMap[minDiff].append([arr[i], arr[i+1]])
            else:
                continue
        return diffMap[minDiff]
            
            
        