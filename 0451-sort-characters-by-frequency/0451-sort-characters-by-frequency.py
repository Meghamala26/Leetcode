class Solution:
    def frequencySort(self, s: str) -> str:
        freqMap={}
        
        for x in s: 
            if x in freqMap:
                freqMap[x]+=1
            else:
                freqMap[x]=1
        
        sortedList=[[] for i in range(max(freqMap.values())+1)]
        
        for key,val in freqMap.items():
            sortedList[val].append(key)
                
        res=''
        
        for freq in range(len(sortedList)):
            for char in sortedList[freq]:
                res+=char*freq
            
        return res[::-1]
        
        
        
        