class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap={}
        ans=[]
        for x in nums:
            if x in freqMap:
                freqMap[x]+=1
            else:
                freqMap[x]=1
        print(freqMap)
        countMap={}
        for key,val in freqMap.items():
            if val in countMap:
                countMap[val].append(key)
            else:
                countMap[val]=[key]
        print(countMap)
                
        freq=list(set(-x for x in freqMap.values()))
        heapq.heapify(freq)
        for i in range(len(freq)):
            
            val=-freq[0]
            print(val)
            heapq.heappop(freq)
            for x in countMap[val]:
                ans.append(x)
            if len(ans)==k:
                break
                
        return ans
        
        
        
        