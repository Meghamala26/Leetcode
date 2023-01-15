class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        result=[]
        interval_list_a,interval_list_b=firstList,secondList
        i,j=0,0
        while(i<len(interval_list_a) and j<len(interval_list_b)):
            if interval_list_a[i][0]<=interval_list_b[j][1] and interval_list_a[i][1]>=interval_list_b[j][0]:
                result.append([max(interval_list_a[i][0],interval_list_b[j][0]),min(interval_list_a[i][1],interval_list_b[j][1])])

            if interval_list_a[i][1]<interval_list_b[j][1]:
                i+=1
            elif interval_list_a[i][1]>interval_list_b[j][1]:
                j+=1
            else:
                i+=1
                j+=1
        return result
