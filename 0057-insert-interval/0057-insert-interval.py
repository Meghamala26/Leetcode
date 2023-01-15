class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_interval=newInterval
        existing_intervals=intervals
        if intervals==[]:
            return [new_interval]
        result=[]
        def findPos():
            low,high=0,len(existing_intervals)-1
            closest=float('-inf')
            while(low<=high):
                mid=(low+high)//2
                if existing_intervals[mid][0]<=new_interval[0]:
                    closest=max(closest,mid)
                    low=mid+1
                else:
                    high=mid-1
            return closest

        def mergeInterval(new):
            if new[0]<=result[-1][1]:
                result[-1][1]=max(new[1],result[-1][1])
            else:
                result.append(new)

        if new_interval[0]<=existing_intervals[0][0]:
            result.append(new_interval)
            pos=-2
        else:
            pos=findPos()
        
        print(pos)
        if pos==len(existing_intervals)-1:
            result=existing_intervals
            mergeInterval(new_interval)
        else:
            for i in range(len(existing_intervals)):
                if i<=pos:
                    result.append(existing_intervals[i])
                elif i==pos+1:
                    mergeInterval(new_interval)
                    mergeInterval(existing_intervals[i])
                else:
                    mergeInterval(existing_intervals[i])


        return result